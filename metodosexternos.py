def mostrarMenu():
    print("|-----------------------------|")
    print("| Elije la opcion que quieras |")
    print("| 0.- Salir                   |")
    print("| 1.- Sumar                   |")
    print("| 2.- Restar                  |")
    print("| 3.- Multiplicar             |")
    print("| 4.- Dividir                 |")
    print("|-----------------------------|")
    opcion = input()
    return opcion
def sumar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado
def restar(numero1, numero2):
    resultado = numero1 - numero2
    return resultado
def multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado
def dividir(numero1, numero2):
    resultado = numero1 / numero2
    return resultado
def pedirnumero1():
    numero1 = int(input())
    return numero1
def pedirnumero2():
    numero2 = int(input())
    return numero2