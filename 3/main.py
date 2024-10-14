import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def actualizar_grafico():
    try:
        selected_variable = variable.get()
        if selected_variable == "fuerza":
            masa = float(entry_masa.get())
            aceleracion = float(entry_aceleracion.get())
            fuerza = masa * aceleracion
            label_resultado.config(text=f"Fuerza: {fuerza:.2f} N")
            ax.clear()
            ax.bar(['Fuerza (N)'], [fuerza], color='skyblue')
        elif selected_variable == "masa":
            fuerza = float(entry_fuerza.get())
            aceleracion = float(entry_aceleracion.get())
            masa = fuerza / aceleracion
            label_resultado.config(text=f"Masa: {masa:.2f} kg")
            ax.clear()
            ax.bar(['Masa (kg)'], [masa], color='skyblue')
        elif selected_variable == "aceleracion":
            fuerza = float(entry_fuerza.get())
            masa = float(entry_masa.get())
            aceleracion = fuerza / masa
            label_resultado.config(text=f"Aceleración: {aceleracion:.2f} m/s²")
            ax.clear()
            ax.bar(['Aceleración (m/s²)'], [aceleracion], color='skyblue')
        canvas.draw()
    except ValueError:
        label_resultado.config(text="Entrada inválida. Use números.")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de la Segunda Ley de Newton")

# Variables
variable = tk.StringVar(value="fuerza")

# Entradas
label_masa = tk.Label(ventana, text="Masa (kg):")
label_masa.grid(row=0, column=0)
entry_masa = tk.Entry(ventana)
entry_masa.grid(row=0, column=1)

label_aceleracion = tk.Label(ventana, text="Aceleración (m/s²):")
label_aceleracion.grid(row=1, column=0)
entry_aceleracion = tk.Entry(ventana)
entry_aceleracion.grid(row=1, column=1)

label_fuerza = tk.Label(ventana, text="Fuerza (N):")
label_fuerza.grid(row=2, column=0)
entry_fuerza = tk.Entry(ventana)
entry_fuerza.grid(row=2, column=1)

# Radio buttons
radio_fuerza = tk.Radiobutton(ventana, text="Calcular Fuerza", variable=variable, value="fuerza")
radio_fuerza.grid(row=3, column=0, columnspan=2)

radio_masa = tk.Radiobutton(ventana, text="Calcular Masa", variable=variable, value="masa")
radio_masa.grid(row=4, column=0, columnspan=2)

radio_aceleracion = tk.Radiobutton(ventana, text="Calcular Aceleración", variable=variable, value="aceleracion")
radio_aceleracion.grid(row=5, column=0, columnspan=2)

# Botón para actualizar el gráfico
boton_actualizar = tk.Button(ventana, text="Actualizar Gráfico", command=actualizar_grafico)
boton_actualizar.grid(row=6, column=0, columnspan=2)

# Resultado
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=7, column=0, columnspan=2)

# Gráfico
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().grid(row=8, column=0, columnspan=2)

ventana.mainloop()