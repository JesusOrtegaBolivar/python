import pyodbc
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
conexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
+ "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
#on premise
# conexion = ("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor
# + "; DATABASE=" + bbdd + "; Trusted_connection=yes")
print("Intentando conectar")
conectado = pyodbc.connect(conexion)
print("conectado")
cursor = conectado.cursor()
sql = "select * from dept"
cursor.execute(sql)
for row in cursor:
    print(row.LOC)


cursor.close()
conectado.close()

