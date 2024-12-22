import requests
url = "https://pokeapi.co/api/v2/pokemon/25"
x = requests.get(url)
data = x.json()

#print(data["game_indices"])
print(data["stats"][0]["base_stat"])
#print(data["sprites"]["back_default"])         





image_url = data["sprites"]["other"]["home"]["front_default"]


response = requests.get(image_url)

if response.status_code == 200:

    with open("downloaded_image.png", "wb") as file:
        file.write(response.content)
    print("Resim başarıyla kaydedildi!")
else:
    print("Resim indirilemedi, hata kodu:", response.status_code)

