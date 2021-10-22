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

# numero1 = 0
# numero2 = 0
# numero3 = 0
# suma = 0
# print("Introduce tres numeros: ")
# numero1 = int(input())
# numero2 = int(input())
# numero3 = int(input())

# if(numero1 > numero2 and numero1 > numero3):
#     print("El numero mayor es: " + str(numero1))
# elif(numero2 > numero1 and numero2 > numero3):
#     print("El numero mayor es: " + str(numero2))
# else:
#     print("El numero mayor es: " + str(numero3))

# if(numero1 < numero2 and numero1 < numero3):
#     print("El numero menor es: " + str(numero1))
# elif(numero2 < numero1 and numero2 < numero3):
#     print("El numero menor es: " + str(numero2))
# else:
#     print("El numero menor es: " + str(numero3))

# if(numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3):
#     print("El numero intermedio es: " + str(numero1))
# elif(numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero1 > numero3):
#     print("El numero intermedio es: " + str(numero2))
# else:
#     print("El numero intermedio es: " +str(numero3))

# suma = numero1 + numero2 + numero3
# print("la suma de todos los numeros es: " + str(suma))


# inicial = int(input("Introduce un numero inicial: "))
# fin = int(input("Introduce el numero final: "))
# for i in range(inicial, fin + 1):
#     if(i % 2 == 0):
#         print("numero par: " + str(i))
#     else:
#         print("numero impar: " + str(i))

# numero = int(input("introduce un numero: "))
# for i in range(1, 10 + 1):
#     print(numero * i)
#     i = i + i


# print("conjetura de collatz")
# numero = int(input("Introduce un numero: "))
# while(numero != 1):
#     if (numero%2 == 0):
#         numero = numero / 2
#     else:
#         numero = numero * 3 + 1
#     print(numero)

# respuesta = "s"
# while(respuesta == "s"):
#     numero = int(input("Introduce un numero: "))
#     if(numero > 0):
#         print("el numero " + str(numero) + " es positivo")
#     elif(numero < 0):
#         print("el numero " + str(numero) + " es negativo")
#     else:
#         print("El numero es 0")
#     respuesta = input("¿Desea continuar? s/n: ")
# print("El programa ha terminado")


# while(True):
#     numero = int(input("Introduce un numero: "))
#     if(numero > 0):
#          print("el numero " + str(numero) + " es positivo")
#     elif(numero < 0):
#          print("el numero " + str(numero) + " es negativo")
#     else:
#          print("El numero es 0")
#     respuesta = input("¿Desea continuar? s/n: ")
#     if(respuesta == "n"):
#         print("El programa ha terminado")
#         break


# texto = "Primer python"
# print("Mayusculas: " + texto.upper())
# print("Replace: " + texto.replace("o", "@"))
# print("Primera letra: " + texto[0])
# print("Longitud texto: " + str(len(texto)))
# print("Buscar letra P: " + str(texto.find("P")))
# print("Buscar siguiente letra p: " + str(texto.find("p", 0)))
# print("Letra p con RFING: " + str(texto.rfind("p")))
# print("Texto iniciando con A: " + str(texto.startswith("A")))
# print("Texto finalizando con n: " + str(texto.endswith("n")))
# print("Texto numeros: " + str(texto.isdigit()))
# print("Texto letras: " + str(texto.isalpha()))
# longitud = len(texto)
# for i in range(longitud):
#     letra = texto[i]
#     print(str(i) + ": " + letra)

# aux = input("Introduce un numero o una letra: ")
# if(aux.isdigit()):
#     print("es un numero")
# else:
#     print("no es un numero")


# email = input("Introduce tu email para la comprobacion: ")
# dominio = (email[email.rfind("."):])
# numerosarroba = ((email.find("@", email.find("@") + 1)))
# arroba = email.find("@")
# punto = email.find(".")
# inicioyfinal = email.startswith("@") + email.startswith(".") + email.endswith(".") + email.endswith("@")
# if((arroba != 1) and (punto != 1) and (inicioyfinal == 0) and (len(dominio) >= 2) and (len(dominio) < 5) and (numerosarroba == -1)       ):
#     print("Correo Valido")
# else:
#     print("correo no valido")

# print("Introduzca su email: ")
# email = input()
# if(email.find("@") == -1):
#     print("Email sin @")
# elif(email.find(".") == -1):
#     print("Email sin punto")
# elif(email.startswith("@") or email.endswith("@")):
#     print("Email iniciado o acabado con @")
# elif(email.startswith(".") or email.endswith(".")):
#     print("Email iniciado o acabado con .")
# elif((email.find("@") != email.rfind("@"))):
#     print("Email con mas de 1 @")
# elif(email.find("@") > email.rfind(".")):
#     print("Se necesita un punto desde de @")
# else:
#     ultimopunto = email.rfind(".")
#     dominio = email[ultimopunto+1:]
#     longitud = len(dominio)
#     if(longitud >= 2 and longitud <= 4):
#         print("Email Correcto")
#     else:
#         print("Dominio incorrecto")


# from math import trunc
# print ("Introduzca su numero de DNI")
# aux = input()
# if(aux.isdigit() == False or len(aux) != 8):
#     print("Se ha introducido mal el DNI")
# else:
#     numerodni = int(aux)
#     resultado = (numerodni - (trunc(numerodni / 23) * 23 ))
#     tabladni = "TRWAGMYFPDXBNJZSQVHLCKET"
#     print("su letra es: " + tabladni[resultado])



# texto = input("Introduce un texto numerico: ")
# suma = 0
# for i in range(len(texto)):
#     caracter = texto[i]
#     caracter = int(caracter)
#     suma = suma + caracter

# print ("la suma es: " + str(suma))


# isbn = input("Introduce un código ISBN: ")
# multiplicacion = 0
# suma = 0
# if((len(isbn) != 10) or (isbn.isdigit() == False)):
#     print("No se ha introducido bien el ISBN")
# else:
#     for i in range(len(isbn)):
#         numero = int(isbn[i])
#         posicion = i + 1
#         multiplicacion = numero * posicion
#         suma = suma + multiplicacion
#     if(suma % 11 == 0 ):
#         print("El ISBN es correcto!")
#     else:
#         print("algo ha salido mal")


# def saludo(nombre):
#     print("Bienvenido: " + nombre)
# def despedida(nombre, fecha):
#     print("Ha sido un placer " + nombre + ", hoy es: " + fecha)
# print("Dinos tu nombre: ")
# nombre = input()
# print("Dinos el dia de la semana")
# fecha = input()
# saludo(nombre)
# despedida(nombre, fecha)


# from metodosexternos import *    

# print("Introduce dos numeros por favor: ")
# numero1 = pedirnumero1()
# numero2 = pedirnumero2()
# valor = -1
# while(valor != 0):
#     valor = int(mostrarMenu())
#     if(valor == 1):
#         resultado = sumar(numero1, numero2)
#         print("El resultado es: " + str(resultado))
#         print("¿Quieres introducir nuevos numeros (s/n)?: ")
#         opcion = input()
#         if(opcion == "s"):
#             print("Introduce dos numeros por favor: ")
#             numero1 = pedirnumero1()
#             numero2 = pedirnumero2()
#         else:
#             print("continuará con los mismo numeros")
#     elif(valor == 2):
#         resultado = restar(numero1, numero2)
#         print("El resultado es: " + str(resultado))
#         print("¿Quieres introducir nuevos numeros (s/n)?: ")
#         opcion = input()
#         if(opcion == "s"):
#             print("Introduce dos numeros por favor: ")
#             numero1 = pedirnumero1()
#             numero2 = pedirnumero2()
#         else:
#             print("continuará con los mismo numeros")
#     elif(valor == 3):
#         resultado = multiplicar(numero1, numero2)
#         print("El resultado es: " + str(resultado))
#         print("¿Quieres introducir nuevos numeros (s/n)?: ")
#         opcion = input()
#         if(opcion == "s"):
#             print("Introduce dos numeros por favor: ")
#             numero1 = pedirnumero1()
#             numero2 = pedirnumero2()
#         else:
#             print("continuará con los mismo numeros")
#     elif(valor == 4):
#         resultado = dividir(numero1, numero2)
#         print("El resultado es: " + str(resultado))
#         print("¿Quieres introducir nuevos numeros (s/n)?: ")
#         opcion = input()
#         if(opcion == "s"):
#             print("Introduce dos numeros por favor: ")
#             numero1 = pedirnumero1()
#             numero2 = pedirnumero2()
#         else:
#             print("continuará con los mismo numeros")
#     else:
#         print("Saliendo del programa...")