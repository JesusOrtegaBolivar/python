import pyodbc
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
conexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
print("conectado")
print("introduce un numero")
numero = input()
print("introduce departamento")
departamento = input()
print("intrudice ciudad")
ciudad = input()
conectado = pyodbc.connect(conexion)
cursor = conectado.cursor()
sql = "insert into dept values (" + numero + ",'" + departamento + "','" + ciudad + "')"
print(sql)
cursor.execute(sql)
print("Rowcount:" + str(cursor.rowcount))

sqlselect = "select dept_no, dnombre, loc from dept"
cursor.execute(sqlselect)
for row in cursor:
    print(row.dnombre + "," + row.loc)

cursor.commit()
cursor.close()
conectado.close()
