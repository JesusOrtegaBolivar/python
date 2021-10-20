# edad = int(input("introduce tu edad: "))
# if(edad >= 18 ):
#     print("eres mayor de edad")
# else:
#     print("Eres menor de edad")


# print("postivo o negativo")
# numero = int(input("introduce un valor: "))
# if (numero > 0):
#     print("el numero es positivo")
# elif (numero == 0):
#     print("el numero es 0")
# else:
#     print("el numero es negativo")


# numero = (int(input("Introduce un numero del 1 al 4: ")))
# if (numero == 1):
#     print("Verano")
# elif (numero == 2):
#     print("otoño")
# elif (numero == 3):
#     print("invierno")
# elif (numero == 4):
#     print("primavera")
# else:
#     print("se ha introducido otro valor")


# numero1 = int(input("introduce un numero: "))
# numero2 = int(input("introduce otro numero: "))
# if(numero1 > numero2):
#     print(numero1, "es mayor que", numero2)
# elif(numero1 < numero2):
#     print(numero1, "es menor que", numero2)
# else:
#     print("los numeros son iguales")


# from math import floor, ceil
# numero1 = 20
# numero2 = 3
# resultado = numero1 / numero2
# print(floor(resultado))
# print(ceil(resultado))


# from math import trunc
# dia = int(input("Introduce tu dia de nacimiento: "))
# mes = int(input("Introduce tu mes de nacimiento: "))
# año = int(input("Introduce tu año de nacimiento: "))

# if(mes == 1):
#     mes = 13
#     año = año - 1
# if(mes == 2):
#     mes = 14
#     año = año - 1

# operacion1 = trunc(((mes + 1)*3)/5)
# operacion2 = trunc(año / 4)
# operacion3 = trunc(año / 100)
# operacion4 = trunc(año / 400)
# operacion5 = trunc(dia + (mes * 2) + año + operacion1 + operacion2 - operacion3 + operacion4 + 2)
# operacion6 = trunc(operacion5 / 7)
# resultado = trunc(operacion5 - (operacion6 * 7))

# if(resultado == 0):
#     print("Sabado")
# elif(resultado == 1):
#     print("domingo")
# elif(resultado == 2):
#     print("Lunes")
# elif(resultado == 3):
#     print("Martes")
# elif(resultado == 4):
#     print("Miercoles")
# elif(resultado == 5):
#     print("Jueves")
# elif(resultado == 6):
#     print("Viernes")
# else:
#     print("Ha ocurrido un error")
