import tkinter as tk
from tkinter import messagebox
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Esta función evaluará la fuerza F en un punto dado x usando la expresión seleccionada
def fuerza_variable(x, expresion):
    try:
        return eval(expresion, {"x": x, "np": np})
    except Exception as e:
        messagebox.showerror("Error", f"Expresión inválida: {e}")
        return 0

# Función para calcular el trabajo y graficar la función al mismo tiempo
def calcular_y_graficar():
    try:
        x0 = float(entry_x0.get())
        x1 = float(entry_x1.get())
        expresion = funciones_var.get()

        # Calcular el trabajo
        trabajo, _ = quad(lambda x: fuerza_variable(x, expresion), x0, x1)
        messagebox.showinfo("Resultado", f"El trabajo es: {trabajo:.2f} J")

        # Graficar la función con área bajo la curva
        x = np.linspace(x0, x1, 400)
        y = [fuerza_variable(xi, expresion) for xi in x]

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f"F(x) = {expresion}", color='blue')
        plt.fill_between(x, y, alpha=0.3, color='skyblue')
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.title("Gráfica de la Fuerza Variable")
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora y Gráfica de Trabajo para Fuerza Variable")

label_funcion = tk.Label(root, text="Selecciona la función F(x):")
label_funcion.grid(row=0, column=0, padx=10, pady=10)

# Menú desplegable con funciones predefinidas
funciones_var = tk.StringVar(root)
funciones_var.set("np.sin(x)")  # Función por defecto
menu_funciones = tk.OptionMenu(root, funciones_var, "np.sin(x)", "np.cos(x)", "x**2", "np.exp(x)", "np.log(x)", "np.tan(x)", "np.sqrt(x)")
menu_funciones.grid(row=0, column=1, padx=10, pady=10)

label_x0 = tk.Label(root, text="Posición inicial (x0):")
label_x0.grid(row=1, column=0, padx=10, pady=10)

entry_x0 = tk.Entry(root)
entry_x0.grid(row=1, column=1, padx=10, pady=10)

label_x1 = tk.Label(root, text="Posición final (x1):")
label_x1.grid(row=2, column=0, padx=10, pady=10)

entry_x1 = tk.Entry(root)
entry_x1.grid(row=2, column=1, padx=10, pady=10)

btn_calcular = tk.Button(root, text="Calcular y Graficar", command=calcular_y_graficar)
btn_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
