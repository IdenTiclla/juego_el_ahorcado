from colorama import Fore, Style
import time

def main():
    nombre = input(Fore.YELLOW + "Ingresa tu nombre: ")
    print(Style.RESET_ALL)
    print(Fore.YELLOW + f"Hola {nombre}, juguemos al ahoracado!")
    print(Style.RESET_ALL)
    print()
    time.sleep(1)
    palabra_secreta = 'simpsons'
    print(Fore.YELLOW + "Comienza a adivinar")
    print(Style.RESET_ALL)
    tu_palabra = ''
    vidas = 5
    while vidas > 0:
        fallas = 0
        for letra in palabra_secreta:
            if letra in tu_palabra:
                print(letra, end="")
            else:
                print("*",end="")
                fallas += 1
        print()
        if fallas == 0:
            print(Fore.GREEN + "Felicidades, ganaste")
            print(Style.RESET_ALL)
            break
        tu_letra = input(Fore.YELLOW + "Introduce una letra: ")
        print(Style.RESET_ALL)
        tu_palabra += tu_letra
        if tu_letra not in palabra_secreta:
            vidas -= 1
            print(Fore.RED + "Equivocacion")
            print(Fore.RED + f"Tu tienes, {vidas} vidas")
            print(Style.RESET_ALL)
        if vidas == 0:
            print(Fore.RED + "Perdiste")
            print(Style.RESET_ALL)
    print(Fore.GREEN + "Gracias por participar")
    print(Style.RESET_ALL)


if __name__ == "__main__":
    main()