def mostrarMenu():
    print("|-----------------------------|")
    print("| Elije la opcion que quieras |")
    print("| 0.- Salir                   |")
    print("| 1.- Bisiesto                |")
    print("| 2.- Narcisista              |")
    print("| 3.- Bisiesto v2             |")
    print("|-----------------------------|")
    opcion = input()
    return opcion

def bisiesto():
    print("Introduce un año para saber si es bisiesto o no: ")
    año = int(input())
    if((año % 4 == 0) and (año % 100 != 0)) or ((año % 4 == 0) and (año % 400 == 0)):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

def narcisista():
    print("Introduce un numero para saber si es un numero narcisista")
    numero = input()
    longitud = len(numero)
    suma = 0
    for i in range(longitud):
        potencia = int(numero[i]) ** int(longitud)
        suma = suma + potencia
    comprobacion = int(numero)
    if(comprobacion == suma):
        print("el numero es narcisista")
    else:
        print("el numero no es narcisista, es normal")

def bisiestosnacimiento():
    print("Introduce el año de tu nacimiento: ")
    nacimiento = int(input())
    print("Introduce el año actual: ")
    año = int(input())
    for i in range(año - nacimiento):
        nacimiento = nacimiento + 1
        if((nacimiento % 4 == 0) and (nacimiento % 100 != 0)) or ((nacimiento % 4 == 0) and (nacimiento % 400 == 0)):
            print("El año: " + str(nacimiento) + " es bisiesto")
    