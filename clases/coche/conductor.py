from coche import Coche
from deportivo import Deportivo
coche = Coche()
coche.marca = "Opel"
coche.modelo = "Astra"
supercar = Deportivo()
supercar.marca = "Ferrari"
supercar.modelo = "F40"
print(coche)
coche.arrancar()
coche.acelerar()
coche.frenar()
coche.detener()
supercar.turbo()