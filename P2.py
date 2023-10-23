from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()

    available_fonts = figlet.getFonts()

    font_name = input("Ingrese el nombre de la fuente o presione Enter para una fuente aleatoria: ")
    if font_name == "":
        font_name = random.choice(available_fonts)
    elif font_name not in available_fonts:
        print("La fuente especificada no está en la lista de fuentes disponibles.")
        return
    
    figlet.setFont(font=font_name)

    text_to_print = input("Ingrese el texto que desea imprimir: ")

    rendered_text = figlet.renderText(text_to_print)
    print(rendered_text)

if __name__ == "__main__":
    main()
