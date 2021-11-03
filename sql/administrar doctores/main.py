from tablemanagement import *
opcion = -1
conecction = ConexionHospital()
while opcion != 6:
    print("-----------------------------")
    print("1.- Insertar Doctor")
    print("2.- Modificar salario Doctor")
    print("3.- Eliminar Doctor")
    print("4.- Buscar Doctor")
    print("5.- Mostrar Doctores")
    print("6.- Salir")
    print("-----------------------------")
    opcion = int(input("-Elije una opcion- "))
    if (opcion == 1):
        print("---Insertar Doctor---")
        print("Introduce el codigo del hospital, numero de doctor, apellido, especializacion y salario")
        print("¡Por orden!")
        hospital_cod = int(input())
        doctor_no = int(input())
        apellido = input()
        especialidad = input()
        salario = int(input())
        respuesta = conecction.insertarDoctor(hospital_cod, doctor_no, apellido, especialidad, salario)
        print("Se han introducido: " + str(respuesta) + " Doctore/s")
    elif (opcion == 2):
        print("---Eliminar Doctor---")
    elif (opcion == 3):
        print("---Eliminar Doctor---")
        print("Introduce numero de doctor que deseas eliminar")
        doctor_no = int(input())
        respuesta = conecction.eliminarDoctor(doctor_no)
        print("Se han eliminado: " + str(respuesta) + "doctor/s")
    elif (opcion == 4):
        print("Buscar doctor")
    elif (opcion == 5):
        print("Mostrar doctores")
    elif (opcion == 6):
        print("Saliendo...")
    else:
        print("Ha ocurrido un error")