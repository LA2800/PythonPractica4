import requests

url = "https://unsplash.com/s/photos/perrito"  

response = requests.get(url)

if response.status_code == 200:
    image_data = response.content

    with open("imagen_descargada.jpg", "wb") as image_file:
        image_file.write(image_data)
else:
    print("No se pudo descargar la imagen. Código de estado:", response.status_code)

import zipfile

zip_filename = "imagen.zip"

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write("imagen_descargada.jpg", "imagen_descargada.jpg")

print(f"La imagen ha sido comprimida en '{zip_filename}'.")

import zipfile

zip_filename = "imagen.zip"

output_directory = "imagen_descomprimida"

import os
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with zipfile.ZipFile(zip_filename, "r") as zipf:
    zipf.extractall(output_directory)

print(f"La imagen ha sido descomprimida en '{output_directory}'.")
