import pyodbc
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
class ConexionHospital:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
    
    def insertarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sqlinsertar = "insert into dept values (?, ?, ?)"
        cursor.execute(sqlinsertar, (numero, nombre, localidad))
        insertar = cursor.rowcount
        cursor.commit()
        cursor.close()
        return insertar
    
    def eliminarDepartamento(self, numero):
        cursor = self.conexion.cursor()
        sqldelete = "delete from dept where dept_no = ?"
        cursor.execute(sqldelete, (numero))
        delete = cursor.rowcount
        cursor.commit()
        cursor.close()
        return delete
    
    def modificarDepartamento(self, numero, nombre, localidad):
        cursor = self.conexion.cursor()
        sqlmodify = "update dept set dnombre = ?, loc = ? where dept_no = ?"
        cursor.execute(sqlmodify, (nombre, localidad, numero))
        modify = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modify
