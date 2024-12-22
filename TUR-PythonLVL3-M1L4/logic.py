import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.attack = None
        self.hp = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data["forms"][0]["name"] 
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()  # Henüz yüklenmemişse bir adın geri alınması
            return f"Pokemonun ismi: {self.name}"
    async def show_img(self):

        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return data["sprites"]["other"]["home"]["front_default"] 
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür
   
             
    async def aattack(self ,enemy):
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            return f"Saldırı Başarılı! @{enemy.name} son canı: @{enemy.hp}" 
        else:
            enemy.hp = 0
            return f"@{enemy.name} yenildi!"

                
    async def get_ID(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    return f"pokemon ID: {self.pokemon_number}" 
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    self.hp = data["stats"][0]["base_stat"]
                    return data["stats"][0]["base_stat"]
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür
                
    async def get_attack(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için eşzamansız bir yöntem
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"  # İstek için URL API'si
        async with aiohttp.ClientSession() as session:  # Bir HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve kodunun çözülmesi
                    self.attack = data["stats"][1]["base_stat"]
                    return data["stats"][1]["base_stat"]
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür
#<>                                                            

"""if __name__ == "__main__":
    pikachu = Pokemon("alex")
    bounsweet = Pokemon("steve")
    pikachu.hp = 35
    pikachu.attack = 55
    bounsweet.hp = 42
    bounsweet.attack = 30
    pikachu.info()
    bounsweet.info()
    print("*"*50)
    pikachu.aattack(bounsweet)"""
