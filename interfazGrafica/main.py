from tkinter import *


#Definicion de funciones
def numeroMayorYmenor():
    ejercicio1 = Toplevel(root)
    ejercicio1.title("New Window")
    ejercicio1.geometry("500x500")
    Label(ejercicio1, text ="Este ejercicio consiste en introducir 3 números para saber cual es mayor").pack()
    Label(ejercicio1, text ="Introduce tres numeros: ").pack()
    numero1 = Entry(ejercicio1, width=50)
    numero1.pack()
    numero2 = Entry(ejercicio1, width=50)
    numero2.pack()
    numero3 = Entry(ejercicio1, width=50)
    numero3.pack()
    def comprobar():


        
        suma = int(numero1.get()) + int(numero2.get()) + int(numero3.get())
        resultado = Label(ejercicio1, text="La suma de todos los numeros es: " + str(suma))
        resultado.pack()
    buton = Button(ejercicio1, text="Comprobar resultado", command=comprobar)
    buton.pack()





root = Tk()
#Creacion de la raiz de la ventana
root.title("Programa")
root.iconbitmap('C:/Users/Jesus/Documents/Estudios/python/interfazGrafica/Emperor.ico')
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
button1 = Button(mainframe, text="Ejercicio 1", command=numeroMayorYmenor)
button1.config(width=25)
button1.pack()



#Creacion del boton para salir anclado abajo
button_quit = Button(root, text="Salir", command=root.quit)
button_quit.config(width=25)
button_quit.pack(side="bottom")
root.mainloop()











