import requests
import sqlite3

def obtener_precio_bitcoin_usd():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        return None

def obtener_tipo_cambio_pen():
    try:
        url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"
        params = {"moneda": "pen"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data["data"][0]["compra"]
    except requests.RequestException:
        return None

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                  fecha TEXT PRIMARY KEY,
                  precio_usd DECIMAL,
                  precio_gbp DECIMAL,
                  precio_eur DECIMAL,
                  precio_pen DECIMAL
                )''')

precio_usd = obtener_precio_bitcoin_usd()

tipo_cambio_pen = obtener_tipo_cambio_pen()

if precio_usd is not None and tipo_cambio_pen is not None:
    cursor.execute("INSERT OR IGNORE INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) VALUES (date('now'), ?, ?, ?, ?)",
                   (precio_usd, precio_usd, precio_usd, precio_usd * tipo_cambio_pen))

conn.commit()
conn.close()

try:
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bitcoin")
    rows = cursor.fetchall()

    if rows:
        print("Contenido de la tabla 'bitcoin':")
        for row in rows:
            print(row)
    else:
        print("La tabla 'bitcoin' está vacía.")

    conn.close()
except sqlite3.Error as se:
    print("Error al mostrar el contenido de la tabla 'bitcoin':", se)

if precio_usd is not None and tipo_cambio_pen is not None:
    precio_compra_10_bitcoins_pen = 10 * precio_usd * tipo_cambio_pen
    precio_compra_10_bitcoins_eur = 10 * precio_usd

    print(f"Precio de comprar 10 Bitcoins en PEN: {precio_compra_10_bitcoins_pen}")
    print(f"Precio de comprar 10 Bitcoins en EUR: {precio_compra_10_bitcoins_eur}")
