import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Función para calcular las energías y graficarlas
def graficar_energia():
    # Parámetros iniciales
    m = float(entry_m.get())  # Masa (kg)
    h0 = float(entry_h.get()) # Altura inicial (m)
    g = 9.81  # Aceleración de la gravedad (m/s^2)

    # Vectores para altura y velocidad
    alturas = np.linspace(0, h0, 100)
    velocidades = np.sqrt(2 * g * (h0 - alturas))  # Velocidad en función de la altura

    # Cálculo de energías
    EK = 0.5 * m * velocidades**2
    EP = m * g * alturas
    Em = EK + EP

    # Limpiamos la figura anterior
    ax.clear()

    # Graficamos las energías
    ax.plot(alturas, EK, label="Energía Cinética (EK)")
    ax.plot(alturas, EP, label="Energía Potencial (EP)")
    ax.plot(alturas, Em, label="Energía Mecánica (Em)", linestyle='--')

    ax.set_xlabel("Altura (m)")
    ax.set_ylabel("Energía (J)")
    ax.set_title("Conservación de la Energía Mecánica")
    ax.legend()

    canvas.draw()

# Configuración de la ventana de Tkinter
root = tk.Tk()
root.title("Conservación de la Energía Mecánica")

# Inputs de masa y altura inicial
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

ttk.Label(frame, text="Masa (kg):").grid(column=0, row=0, sticky="w")
entry_m = ttk.Entry(frame, width=10)
entry_m.grid(column=1, row=0, sticky="e")

ttk.Label(frame, text="Altura inicial (m):").grid(column=0, row=1, sticky="w")
entry_h = ttk.Entry(frame, width=10)
entry_h.grid(column=1, row=1, sticky="e")

# Botón para graficar
ttk.Button(frame, text="Graficar Energías", command=graficar_energia).grid(column=0, row=2, columnspan=2, pady=10)

# Configuración de Matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=1, column=0)

root.mainloop()
