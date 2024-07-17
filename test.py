import tkinter as tk
from tkinter import ttk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de etiqueta con cadena")

# Variable de tipo cadena
mi_cadena = "¡Hola, mundo!"

# Crear una etiqueta y mostrar la cadena
etiqueta = ttk.Label(ventana, text=mi_cadena, font=("Arial", 14))
etiqueta.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
