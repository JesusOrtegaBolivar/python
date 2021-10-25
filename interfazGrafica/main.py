from tkinter import *

#Definicion de funciones
def numeroMayorYmenor():
    ejercicio = Toplevel(root)
    ejercicio.title("Organizar numeros")
    ejercicio.geometry("500x500")
    Label(ejercicio, text ="Este ejercicio consiste en introducir 3 números para saber cual es mayor").pack()
    Label(ejercicio, text ="Introduce tres numeros: ").pack()
    x1 = Entry(ejercicio, width=50)
    x1.pack()
    x2 = Entry(ejercicio, width=50)
    x2.pack()
    x3 = Entry(ejercicio, width=50)
    x3.pack()
    def comprobar():
        numero1 = int(x1.get())
        numero2 = int(x2.get())
        numero3 = int(x3.get())
        suma = numero1 + numero2 + numero3
        if(numero1 > numero2 and numero1 > numero3):
            resultado = Label(ejercicio, text="El numero: " + str(numero1) + " es mayor")
            resultado.pack()
        elif(numero2 > numero1 and numero2 > numero3):
            resultado = Label(ejercicio, text="El numero: " + str(numero2) + " es mayor")
            resultado.pack()
        elif(numero3 > numero1 and numero3 > numero2):
            resultado = Label(ejercicio, text="El numero: " + str(numero3) + " es mayor")
            resultado.pack()

        if(numero1 > numero2 and numero1 < numero3 or numero1 < numero2 and numero1 > numero3):
            resultado = Label(ejercicio, text="El numero intermedio es: " + str(numero1) )
            resultado.pack()
        elif(numero2 > numero1 and numero2 < numero3 or numero2 < numero1 and numero1 > numero3):
            resultado = Label(ejercicio, text="El numero intermedio es: " + str(numero2))
            resultado.pack()
        else:
            resultado = Label(ejercicio, text="El numero intermedio es: " + str(numero3))
            resultado.pack()
        resultado = Label(ejercicio, text="La suma de todos los numeros es: " + str(suma))
        resultado.pack()
    buton = Button(ejercicio, text="Comprobar resultado", command=comprobar)
    buton.pack()

def numerospares():
    ejercicio = Toplevel(root)
    ejercicio.title("Numeros pares")
    ejercicio.geometry("500x500")
    Label(ejercicio, text ="Este ejercicio consiste en un numero inicial y un numero final, para separarlos en pares e impares").pack()
    Label(ejercicio, text ="Introduce el numero inicial y final: ").pack()
    scrollbar = Scrollbar(ejercicio)
    scrollbar.config( command = ejercicio.yview )
    scrollbar.pack( side = RIGHT, fill = Y )

    x1 = Entry(ejercicio, width=50)
    x1.pack()
    x2 = Entry(ejercicio, width=50)
    x2.pack()
    def comprobar():
        inicial = int(x1.get())
        final = int(x2.get())
        for i in range(inicial, final + 1):
            if(i % 2 == 0):
                resultado = Label(ejercicio, text="El numero: " + str(i) + " es par")
                resultado.pack()
            else:
                resultado = Label(ejercicio, text="El numero: " + str(i) + " es impar")
                resultado.pack()
    buton = Button(ejercicio, text="Comprobar resultado", command=comprobar)
    buton.pack()







root = Tk()
#Creacion de la raiz de la ventana
root.title("Programa")
#root.iconbitmap('C:/Users/Jesus/Documents/Estudios/python/interfazGrafica/Emperor.ico')
root.geometry("500x500")
root.config(bg="#EBECF4")

#Creacion de un frame
mainframe = Frame()
mainframe.config(bg="#FFFFFF", bd=15, relief="groove", width="650px", height="350px", cursor="hand2")
mainframe.pack(side="top")


#Texto informativo
label = Label(mainframe, text="Muestrario de Ejercicios")
label.config(bg="#FFFFFF")
label.pack()

#Botones para los ejercicios
button = Button(mainframe, text="Organizar números", command=numeroMayorYmenor)
button.config(width=25)
button.pack(pady=5)
button = Button(mainframe, text="Numeros pares", command=numerospares)
button.config(width=25)
button.pack(pady = 5)



#Creacion del boton para salir anclado abajo
button_quit = Button(root, text="Salir", command=root.quit)
button_quit.config(width=25)
button_quit.pack(side="bottom")
root.mainloop()











