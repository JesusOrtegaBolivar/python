from conexion import *
respuesta = -1
connection = ConexionHospital()
while respuesta != 4:
    print("1.- nuevo departamento")
    print("2.- Eliminar departamento")
    print("3.- Modificar departamento")
    print("4.- Buscar departamento")
    print("5.- Salir")
    respuesta = int(input())
    if (respuesta == 1):
        print("Introduce el numero de departamento")
        numero = int(input())
        print("Introduce el nombre de departamento")
        nombre = input()
        print("Introduce la localidad de departamento")
        localidad = input()
        respuesta = connection.insertarDepartamento(numero, nombre, localidad)
        print("Departamento introducido: " + str(respuesta))
    elif(respuesta == 2):
        print("Introduce el numero de departamento que quieres eliminar: ")
        numero = int(input())
        respuesta = connection.eliminarDepartamento(numero)
        print("Departamento introducido: " + str(respuesta))
    elif(respuesta == 3):
        print("Introduce el numero de departamento que quieres modificar: ")
        numero = int(input())
        print("Nuevo nombre")
        nombre = input()
        print("Nueva localidad")
        localidad = input()
        respuesta = connection.modificarDepartamento(numero, nombre, localidad)
        print("Departamento introducido: " + str(respuesta))
    elif(respuesta == 4):
        print("Introduce el numero de departamento que quieras buscar:")
        numero = int(input())
        respuesta = connection.buscarDepartamento(numero)
        if (not respuesta):
            print("No existe departamento")
        else:
            print(respuesta)
    elif(respuesta == 5):
        print("Saliendo")
    else:
        print("error")