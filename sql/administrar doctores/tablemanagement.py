import pyodbc
servidor = "LOCALHOST\SQLEXPRESS"
bbdd = "HOSPITAL"
usuario = "SA"
password = "azure"
class ConexionHospital:
    def __init__(self):
        self.conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + servidor + "; DATABASE=" + bbdd + "; UID=" + usuario + ";PWD=" + password)
    
    def insertarDoctor(self, hospital_cod, doctor_no, apellido, especialidad, salario):
        cursor = self.conexion.cursor()
        sqlinsertar = "insert into doctor values (?, ?, ?, ?, ?)"
        cursor.execute(sqlinsertar, (hospital_cod, doctor_no, apellido, especialidad, salario))
        insertar = cursor.rowcount
        cursor.commit()
        cursor.close()
        return insertar
    def eliminarDoctor(self, doctor_no):
        cursor = self.conexion.cursor()
        sqldelete = "delete from doctor where doctor_no = ?"
        cursor.execute(sqldelete, (doctor_no))
        delete = cursor.rowcount
        cursor.commit()
        cursor.close()
        return delete
    def modificarDoctor(self, doctor_no):
        cursor = self.conexion.cursor()
        sqldelete = "delete from doctor where doctor_no = ?"
        cursor.execute(sqldelete, (doctor_no))
        delete = cursor.rowcount
        cursor.commit()
        cursor.close()
        return delete
    