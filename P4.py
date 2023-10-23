import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price_usd = data["bpi"]["USD"]["rate_float"]
except requests.RequestException as e:
    print("Error al obtener los datos de precio de Bitcoin:", e)
    price_usd = None


if price_usd is not None:
    filename = "precio_bitcoin.txt"

    data_to_write = f"Fecha: {data['time']['updated']} USD: {price_usd:.4f}\n"

    with open(filename, "a") as file:
        file.write(data_to_write)
    print(f"Los datos de precio de Bitcoin se han guardado en '{filename}'.")
else:
    print("No se pudieron almacenar los datos debido a un error en la solicitud.")
