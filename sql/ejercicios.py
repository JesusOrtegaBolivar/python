# #Incrementar salario empleados
# import pyodbc
# servidor = "LOCALHOST\SQLEXPRESS"
# bbdd = "HOSPITAL"
# usuario = "SA"
# password = "azure"
# conexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
# + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
# print("conectado")
# conectado = pyodbc.connect(conexion)
# cursor = conectado.cursor()
# print("¿El salario de que oficio quieres incrementar?")
# oficio = input()
# print("¿Cuanto quieres incrementar el salario?")
# incremento = int(input())
# sql = "update emp set salario = salario + ? where oficio = ?"
# cursor.execute(sql, (incremento, oficio))
# print("Han sido modificados: " + str(cursor.rowcount) + " empleados")
# cursor.commit()
# sqlselect = "select apellido, oficio, salario from emp where oficio = ?"
# cursor.execute(sqlselect, (oficio))
# for row in cursor:
#     print("Nombre: " + row.apellido + " Oficio: " + row.oficio + " Salario: " + str(row.salario))

# #Aplicacion para eliminar a los enfermos
# import pyodbc
# servidor = "LOCALHOST\SQLEXPRESS"
# bbdd = "HOSPITAL"
# usuario = "SA"
# password = "azure"
# conexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
# + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
# print("conectado")
# conectado = pyodbc.connect(conexion)
# cursor = conectado.cursor()
# sqlselect = "select inscripcion, apellido from enfermo"
# cursor.execute(sqlselect)
# for row in cursor:
#     print("Nombre: " + row.apellido + " ---- " +" Inscripcion: " + row.inscripcion)
# print("¿Que enfermo quieres eliminar?")
# inscripcion = int(input())
# sqldelete = "delete from enfermo where inscripcion = ?"
# cursor.execute(sqldelete,(inscripcion))
# cursor.commit()

# #ahora lo mismo pero con clases
# from conexionhospital import *
# connection = ConexionHospital()
# print("¿Que enfermo quieres eliminar?")
# inscripcion = int(input())
# respuesta = connection.eliminarEnfermo(inscripcion)
# print("Resgristro eliminados: " + str(respuesta))
# #A continuacion vamos a modificar el apellido de un enfermo
# print("Modificar apellido de un enfermo. Introducir apellido e inscripcion")
# apellido = input()
# inscripcion = int(input())
# respuesta = connection.modificarEnfermo(apellido, inscripcion)
# print("Registros modificados: " + str(respuesta))

