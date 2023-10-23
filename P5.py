def guardar_tabla_de_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    with open(f"tabla-{numero}.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{numero} x {i} = {numero * i}\n")
    print(f"La tabla de multiplicar del {numero} se ha guardado en tabla-{numero}.txt")

def mostrar_tabla_de_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            tabla = archivo.read()
            print(f"Tabla de multiplicar del {numero}:\n{tabla}")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_de_tabla(numero, linea):
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return

    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= linea:
                print(lineas[linea - 1].strip())
            else:
                print(f"No hay una línea {linea} en el archivo tabla-{numero}.txt")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def main():
    while True:
        print("Menú:")
        print("1. Guardar tabla de multiplicar en un archivo")
        print("2. Mostrar tabla de multiplicar desde un archivo")
        print("3. Mostrar una línea de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Elija una opción (1/2/3/4): ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            guardar_tabla_de_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_de_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea (1-10): "))
            mostrar_linea_de_tabla(numero, linea)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
