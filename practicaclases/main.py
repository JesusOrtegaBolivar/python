from persona import Persona
print("Ejemplo clase persona")

person = Persona()
person.nombre = "Jesús"
person.apellidos = "Ortega Bolívar"
person.pais = "España"
person.fechanacimiento = 1997
print(person.getNombreCompleto())
print("Su edad es: " + str(person.getEdad()))
print(person)