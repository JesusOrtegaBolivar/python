def dividirNumeros():
    try:
        print("introduzca dos numeros: ")
        numero1 = int(input())
        numero2 = int(input())
        print("El resultado de la division es: " + str((numero1/numero2)))
    except ValueError:
        print("Error, Debes introducir un numero")
    except ZeroDivisionError:
        print("No puedes dividir entre zero")
    except:
        print("Error general")
    finally:
        print("Siempre me ejecuto")

dividirNumeros()