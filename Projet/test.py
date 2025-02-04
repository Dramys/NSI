import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import os

def solve_linear():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            messagebox.showerror("Erreur", "a ne peut pas être égal à 0")
            return
        x1 = -b / a
        result_label.config(text=f"Solution: x = {x1:.2f}")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            messagebox.showerror("Erreur", "a ne peut pas être égal à 0")
            return
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = (-b - np.sqrt(delta)) / (2 * a)
            x2 = (-b + np.sqrt(delta)) / (2 * a)
            result_label.config(text=f"Solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
        elif delta == 0:
            x1 = -b / (2 * a)
            result_label.config(text=f"Solution unique: x = {x1:.2f}")
        else:
            result_label.config(text="Pas de solution réelle")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

def plot_graph():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get()) if equation_type.get() == 2 else 0
        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c if equation_type.get() == 2 else a*x + b
        plt.figure(figsize=(5, 4))
        plt.plot(x, y, label=f"f(x) = {a}x^2 + {b}x + {c}" if equation_type.get() == 2 else f"f(x) = {a}x + {b}")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.show()
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

def update_ui():
    if equation_type.get() == 1:
        label_c.grid_remove()
        entry_c.grid_remove()
        solve_button.config(command=solve_linear)
    else:
        label_c.grid()
        entry_c.grid()
        solve_button.config(command=solve_quadratic)

# Interface graphique
root = tk.Tk()
root.title("Résolveur d'équation")
root.geometry("175x250")
root.resizable(False, False)

frame = ttk.Frame(root, padding=10)
frame.pack(fill=tk.BOTH, expand=True)

equation_type = tk.IntVar(value=1)
ttk.Label(frame, text="Type d'équation :").grid(row=0, column=0, columnspan=2)
ttk.Radiobutton(frame, text="1er degré (ax+b=0)", variable=equation_type, value=1, command=update_ui).grid(row=1, column=0, columnspan=2)
ttk.Radiobutton(frame, text="2nd degré (ax²+bx+c=0)", variable=equation_type, value=2, command=update_ui).grid(row=2, column=0, columnspan=2)

# Champs d'entrée
label_a = ttk.Label(frame, text="a:")
label_a.grid(row=3, column=0)
entry_a = ttk.Entry(frame, width=7)
entry_a.grid(row=3, column=1)

label_b = ttk.Label(frame, text="b:")
label_b.grid(row=4, column=0)
entry_b = ttk.Entry(frame, width=7)
entry_b.grid(row=4, column=1)

label_c = ttk.Label(frame, text="c:")
label_c.grid(row=5, column=0)
entry_c = ttk.Entry(frame, width=7)
entry_c.grid(row=5, column=1)

solve_button = ttk.Button(frame, text="Résoudre", command=solve_linear)
solve_button.grid(row=6, column=0, columnspan=2, pady=5)

plot_button = ttk.Button(frame, text="Afficher la courbe", command=plot_graph)
plot_button.grid(row=7, column=0, columnspan=2, pady=5)

result_label = ttk.Label(frame, text="", font=("Arial", 10, "bold"))
result_label.grid(row=8, column=0, columnspan=2)

update_ui()
root.mainloop()