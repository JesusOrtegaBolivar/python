from mes import Mes
print("Programa que mostrara meses")
mes = ""
listameses = []
for i in range(1, 13):
    mes = Mes(str(i))
    mes.temperatura()
    listameses.append(mes)

for obj in listameses:
    nombre = obj.nombre
    maxima = obj.maxima
    minima = obj.minima
    media = obj.media
    print("Nombre: " + str(nombre) + " Temperatura máxima: " + str(maxima) + " Temperatura mínima: " + str(minima) + "  Temperatura media: " + str(media))
    

