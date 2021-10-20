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

email = input("Introduce tu email para la comprobacion: ")
posicion = email.rfind(".")
dominio = (email[posicion:])
arroba = ((email.find("@", email.find("@") + 1)))
if((email.find("@")) != -1):
    if((email.find(".")) != -1):
        if(email.startswith("@") == False) and (email.startswith(".") == False) and (email.endswith(".") == False) and (email.endswith("@") == False) :
            if(len(dominio) >= 2) and (len(dominio) < 5):
                if(arroba != -1):
                    print("el correo es invalido")
                else:
                    print("el correo es valido")
            else:
                print("el correo es invalido")
        else:
            print("el correo es invalido")
    else:
        print("el correo es invalido")
else:
    print("El email no es valido")
