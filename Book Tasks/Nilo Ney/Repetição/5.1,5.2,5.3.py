# utilizarei uma função recursiva
import time


def aumenta(numero, limite, intervalo):
    print(numero)
    time.sleep(intervalo)
    numero += 1

    if numero <= limite:
        aumenta(numero, limite, intervalo)
        if numero == limite:
            print("Fogo!!")


# numero = int(input("digite um número:  "))
# agumenta(numero)

aumenta(1,100, 0.05)