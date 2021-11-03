import pyodbc
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
class ConexionHospital:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
    
    def eliminarEnfermo(self, inscripcion):
        cursor = self.conexion.cursor()
        sqldelete = "delete from enfermo where inscripcion = ?"
        cursor.execute(sqldelete, (inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados
    def modificarEnfermo(self, apellido, inscripcion):
        cursor = self.conexion.cursor()
        sqlmodify = "update enfermo set apellido = ? where inscripcion = ?"
        cursor.execute(sqlmodify,(apellido, inscripcion))
        modificados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return modificados
