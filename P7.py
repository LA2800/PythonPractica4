import requests
import sqlite3

url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

params = {
    "moneda": "usd",
    "anio": 2023
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                      fecha TEXT PRIMARY KEY,
                      compra DECIMAL,
                      venta DECIMAL
                    )''')

    for item in data["data"]:
        fecha = item["fecha"]
        compra = item["compra"]
        venta = item["venta"]
        cursor.execute("INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)",
                       (fecha, compra, venta))
    conn.commit()
    conn.close()

    print("Datos almacenados en la tabla 'sunat_info'.")
except requests.RequestException as e:
    print("Error al obtener los datos de la API de SUNAT:", e)
except sqlite3.Error as se:
    print("Error al trabajar con la base de datos:", se)

try:
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sunat_info")
    rows = cursor.fetchall()

    if rows:
        print("Contenido de la tabla 'sunat_info':")
        for row in rows:
            print(row)
    else:
        print("La tabla 'sunat_info' está vacía.")
    
    conn.close()
except sqlite3.Error as se:
    print("Error al mostrar el contenido de la tabla:", se)
