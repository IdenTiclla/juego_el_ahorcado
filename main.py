import time

def main():
    nombre = input("Ingresa tu nombre: ")
    print(f"Hola {nombre}, juguemos al ahoracado!")
    print()
    time.sleep(1)
    palabra_secreta = 'simpsons'
    print("Comienza a adivinar")
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
            print("Felicidades, ganaste")
            break
        tu_letra = input("Introduce una letra: ")
        tu_palabra += tu_letra
        if tu_letra not in palabra_secreta:
            vidas -= 1
            print("Equivocacion")
            print(f"Tu tienes, {vidas} vidas")
        if vidas == 0:
            print("Perdiste")
    print("Gracias por participar")
        


if __name__ == "__main__":
    main()