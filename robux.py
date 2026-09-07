import tkinter as tk
from tkinter import messagebox
import random

intentos_cierre = 0
clicks_boton = 0
meta_clicks = 50

def intentar_cerrar():
    global intentos_cierre, clicks_boton
    
    # Si ya empezó el minijuego, la X de arriba avisa cuántos clics llevas y no te deja salir
    if clicks_boton > 0:
        messagebox.showwarning("ERROR", f"¡No puedes salir! Consigue {meta_clicks} clicks. Llevas {clicks_boton}.")
        return

    intentos_cierre += 1
    
    if intentos_cierre == 1:
        messagebox.showinfo("Mensaje 1", "Estudia bro")
    elif intentos_cierre == 2:
        messagebox.showinfo("Mensaje 2", "¡Que estudies te dije! 📚")
    elif intentos_cierre == 3:
        messagebox.showinfo("Mensaje 3", "Na mentira bro\n\n¡Ahora juega para salir! 😂")
        
        # Transformamos el botón gigante verde en el botonsito rojo escurridizo
        boton_robux.config(
            text="Robux 🤑", 
            font=("Arial", 9, "bold"), 
            bg="red", 
            fg="white", 
            command=registrar_click  # Cambia la acción para que sume clics de verdad
        )
        mover_boton()

def registrar_click():
    global clicks_boton
    clicks_boton += 1
    
    if clicks_boton >= meta_clicks:
        messagebox.showinfo("¡LIBRE!", "felicidades bro liberate de esto")
        ventana.destroy()
    else:
        mover_boton()

def mover_boton():
    # Actualiza el texto en la pantalla con el contador real
    etiqueta.config(text=f"Clicks logrados: {clicks_boton} / {meta_clicks}", font=("Arial", 14, "bold"))
    
    # Mueve el botón a una posición totalmente al azar
    nuevo_x = random.randint(20, 360)
    nuevo_y = random.randint(80, 240)
    boton_robux.place(x=nuevo_x, y=nuevo_y)

def presionar_boton_inicio():
    intentar_cerrar()

ventana = tk.Tk()
ventana.title("Ventana para conseguir robux infinitos LOL")
ventana.geometry("450x300")
ventana.resizable(False, False)

# Reemplazamos la X para usar nuestro sistema de seguridad
ventana.protocol("WM_DELETE_WINDOW", intentar_cerrar)

etiqueta = tk.Label(ventana, text="Mira toca aqui para robux infinitos gratis", font=("Arial", 12))
etiqueta.pack(pady=30)

boton_robux = tk.Button(
    ventana, 
    text="¡Bro no te vayas si quieres te doy mas robux gratuitos! 🤑", 
    command=presionar_boton_inicio, 
    bg="green", 
    fg="white", 
    font=("Arial", 10, "bold")
)
boton_robux.pack(pady=20)

ventana.mainloop()

