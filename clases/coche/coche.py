class Coche:
    marca = ""
    modelo = ""
    velocidad = 0
    estado = False
    def arrancar(self):
        self.estado = True
        print("Arrancando coche")
    def acelerar(self):
        if(self.estado == False):
            print("primero debes de arrancar el coche")
        else:
            self.velocidad = self.velocidad + 20
            print("Has acelerado hasta: " + str(self.velocidad) + " Km/h")
        print("Velocidad actual: " + str(self.velocidad) + " Km/h")
    def frenar(self):
        if(self.velocidad == 0):
            print("El coche esta detenido")
        else:
            self.velocidad = self.velocidad - 10
            print("Has frenado hasta: " + str(self.velocidad) + " Km/h")
        print("Velocidad actual: " + str(self.velocidad) + " Km/h")
    def detener(self):
        self.estado = False
        self.velocidad = 0
        print("Deteniendo coche")
    def __str__(self):
        return "Coche marca: " + self.marca + " Modelo: " + self.modelo

        