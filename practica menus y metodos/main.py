from metodos import *
import time
opcion = int(mostrarMenu())

if(opcion == 1):
    bisiesto()
elif(opcion == 2):
    narcisista()
elif(opcion == 3):
    bisiestosnacimiento()
elif(opcion == 0):
    print("Saliendo del programa")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
else:
    print("Ha ocurrido un error, saliendo del programa")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")