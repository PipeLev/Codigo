from tkinter import *
import tkinter.messagebox

# Creamos la ventana principal
root = Tk() 

# Título y tamaño de la ventana
root.title("Que tal")
root.geometry('500x300')

def hola():
    tkinter.messagebox.showinfo("Saludo", "¡Hola! ¿Cómo estás?")

# Añadimos un botón para poder probar la función
boton = Button(root, text="Haz clic aquí", command=hola)
boton.pack(pady=50)


root.mainloop()