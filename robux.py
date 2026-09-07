import tkinter as tk
from tkinter import messagebox
import random

intentos_cierre = 0
clicks_boton = 0
meta_clicks = 50
fase_dos = False

def intentar_cerrar():
    global intentos_cierre, clicks_boton, meta_clicks
    
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
        clicks_boton = 0
        boton_robux.config(text="Robux 🤑", font=("Arial", 9, "bold"), bg="red", fg="white", command=registrar_click)
        mover_boton()

def registrar_click():
    global clicks_boton, meta_clicks, fase_dos
    clicks_boton += 1
    
    if clicks_boton >= meta_clicks:
        if not fase_dos:
            messagebox.showinfo("¡LIBRE!", "felicidades bro liberate de esto")
            messagebox.showwarning("TROLEADO", "NAH MENTIRA AHORA TENDRAS QUE HACER 255 CLICKS PARA LIBERARTE ESO TE PASA POR NO ESTUDIAR")
            meta_clicks = 255
            fase_dos = True
            mover_boton()
        else:
            messagebox.showwarning("FINAL BOSS", "¡¿Pensaste que era tan fácil?! ¡Cierra las 45 pestañas de estudio! 😈")
            ventana.withdraw()  # Oculta la principal pero mantiene vivo el programa
            abrir_ventanas_locas()
    else:
        mover_boton()

def mover_boton():
    etiqueta.config(text=f"Clicks logrados: {clicks_boton} / {meta_clicks}", font=("Arial", 14, "bold"))
    nuevo_x = random.randint(20, 360)
    nuevo_y = random.randint(80, 240)
    boton_robux.place(x=nuevo_x, y=nuevo_y)

def abrir_ventanas_locas():
    ventanas_abiertas = 45

    def restar_ventana():
        global ventanas_abiertas
        ventanas_abiertas -= 1
        if ventanas_abiertas <= 0:
            ventana.destroy()  # Cierra el programa por completo cuando quitan la última

    for i in range(1, 46):
        sub_ventana = tk.Toplevel()
        sub_ventana.title(f"Castigo {i}/45")
        sub_ventana.geometry("300x150")
        
        pos_x = random.randint(100, 1000)
        pos_y = random.randint(100, 700)
        sub_ventana.geometry(f"+{pos_x}+{pos_y}")
        sub_ventana.resizable(False, False)
        
        # Si cierran una subventana, descuenta del contador
        sub_ventana.protocol("WM_DELETE_WINDOW", lambda sv=sub_ventana: [sv.destroy(), restar_ventana()])
        
        tk.Label(
            sub_ventana, 
            text=f"Ventana {i} de 45\n\n¡PUEDES LOGRARLO BRO! 📚💻", 
            font=("Arial", 11, "bold"), 
            fg="red"
        ).pack(pady=30)

def presionar_boton_inicio():
    intentar_cerrar()

ventana = tk.Tk()
ventana.title("Ventana para conseguir robux infinitos LOL")
ventana.geometry("450x300")
ventana.resizable(False, False)

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


