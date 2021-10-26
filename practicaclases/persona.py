class Persona:
    nombre = ""
    apellidos = ""
    fechanacimiento = 0
    pais = ""
    def __init__(self):
        #Se le indican valores al iniciar
        self.pais = "Francia"
    def __str__(self):
        return self.nombre + " " + self.apellidos + " Pais: " + self.pais + " Edad: " + str(self.getEdad())
    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos
    def getNacionalidad(self):
        return self.pais
    def getEdad(self):
        return 2021 - self.fechanacimiento