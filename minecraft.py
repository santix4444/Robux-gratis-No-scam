import tkinter as tk

ventana = tk.Tk()
ventana.title("Ventana para conseguir robux infinitos LOL")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana,
                       text="Mira toca aqui para robux infinitos gratis")
etiqueta.pack()

ventana.mainloop()
import tkinter as tk
from tkinter import messagebox

def conseguir_robux():
    messagebox.showwarning("¡ATRAPADO!", "¡Felicidades! Acabas de caer en la trampa. No existen los Robux infinitos. ¡A trabajar! 😂")

ventana = tk.Tk()
ventana.title("Ventana para conseguir robux infinitos LOL")
ventana.geometry("400x300")

etiqueta = tk.Label(ventana, text="Mira toca aqui para robux infinitos gratis", font=("Arial", 12))
etiqueta.pack(pady=20)

boton_robux = tk.Button(ventana, text="🤑 ¡CONSEGUIR ROBUX YA! 🤑", command=conseguir_robux, bg="green", fg="white", font=("Arial", 10, "bold"))
boton_robux.pack(pady=20)

ventana.mainloop()
