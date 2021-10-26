import random
class Mes:
    nombre = ""
    maxima = -1
    minima = -1
    media = -1
    def temperatura(self):
        x1 = random.randint(-10, 40)
        x2 = random.randint(-10, 40)
        if(x1 > x2):
            self.maxima = x1
            self.minima = x2
            self.media = (self.maxima + self.minima) / 2
        else:
            self.maxima = x2
            self.minima = x1
            self.media = (self.maxima + self.minima) / 2
    def __init__(self, nombre):
        self.nombre = "Mes " + str(nombre)
    
