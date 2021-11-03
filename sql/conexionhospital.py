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
        sqldelete = "delete from enfermo where inscripcionn = ?"
        cursor.execute(sqldelete, (inscripcion))
        eliminados = cursor.rowcount
        cursor.commit()
        cursor.close()
        return eliminados
