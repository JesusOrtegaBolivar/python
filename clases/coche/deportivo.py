from coche import Coche
class Deportivo(Coche):
    def turbo(self):
        self.velocidad = self.velocidad + 80
        print("Activando turbo " + str(self.velocidad))