import requests

def main():
    try:
        n = int(input("Por favor, ingrese la cantidad de Bitcoins que posee: "))
        if n < 0:
            print("La cantidad de Bitcoins no puede ser negativa.")
            return

        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        
        response.raise_for_status()

        data = response.json()
        price_in_usd = data["bpi"]["USD"]["rate_float"]

        cost_in_usd = n * price_in_usd

        print(f"El costo actual de {n} Bitcoins es ${cost_in_usd:,.4f} USD")

    except ValueError:
        print("Por favor, ingrese un valor válido para la cantidad de Bitcoins.")
    except requests.RequestException:
        print("Se produjo un error al hacer la solicitud a la API de CoinDesk.")

if __name__ == "__main":
    main()
