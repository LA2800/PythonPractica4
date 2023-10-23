def contar_lineas_de_codigo(archivo):
    try:
        with open(archivo, "r") as f:
            lineas = f.readlines()
            lineas_de_codigo = 0
            en_comentario = False

            for linea in lineas:
                linea = linea.strip()  # Eliminar espacios en blanco al principio y al final

                if not en_comentario:
                    if linea.startswith("#"):
                        continue  # Saltar comentarios
                    elif linea.startswith("'''") or linea.startswith('"""'):
                        en_comentario = True
                        continue

                if en_comentario and (linea.endswith("'''") or linea.endswith('"""')):
                    en_comentario = False
                    continue

                if not linea:  # Línea en blanco
                    continue

                lineas_de_codigo += 1

            return lineas_de_codigo

    except FileNotFoundError:
        return None

def main():
    archivo = input("Ingrese la ruta del archivo .py: ")
    if archivo.endswith(".py"):
        lineas_de_codigo = contar_lineas_de_codigo(archivo)
        if lineas_de_codigo is not None:
            print(f"Número de líneas de código en '{archivo}': {lineas_de_codigo}")
        else:
            print(f"El archivo '{archivo}' no se encontró.")
    else:
        print("El archivo no tiene extensión .py válida.")

if __name__ == "__main__":
    main()
