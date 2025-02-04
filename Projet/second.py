
import math
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import sympy as sp

window = Tk()

window.geometry("200x225")

window.title("Résolveur d'équation")

window.resizable(False, False)

window.iconbitmap("calculatrice.ico")

window.configure(bg="#fcbf49")

def execute():

    v1 = var1.get()
    v2 = var2.get()
    v3 = var3.get()
    v4 = var4.get()

    print(v1,v2,v3,v4)

    a = float(inta.get())

    assert a != 0, 'a ne peut pas être égal à 0'

    b = float(intb.get())
    c = float(intc.get())

    delta = b**2 - 4 * a * c

    solutions = []

    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        solutions.append(x1)
        solutions.append(x2)

    if delta == 0:
        x1 = (-b) / (2 * a)
        x2 = ""
        solutions.append(x1)
        solutions.append(x2)

    if delta < 0:
        t1 = str(-b)
        t2 = 'i'
        t3 = str(math.sqrt(abs(delta)))
        t4 = str(2 * a)
        x1 = '(' + t1 + ' - ' + t2 + t3 + ') / ' + t4
        x2 = '(' + t1 + ' + ' + t2 + t3 + ') / ' + t4
        solutions.append(x1)
        solutions.append(x2)

    print('Équation : ' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c) + ' = 0')
    print('Discriminant :', delta)
    print('Solution(s) :', solutions)

    if v3 == 1:

        window3 = Tk()

        window3.geometry("250x100")

        window3.title('f(x) = ' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c))

        window3.resizable(False, False)

        window3.iconbitmap("calculatrice.ico")

        window3.configure(bg="#fcbf49")

        x = sp.symbols('x')
        f = a*x**2+b*x+c
        derive = sp.diff(f, x)

        title = Label(window3, text="La dérivée première est :", bg="#fcbf49")
        der = Label(window3, text=str(derive), bg="#fcbf49")
        title.grid(column=0, row=0)
        der.grid(column=0, row=1)

    if v4 == 1:

        window4 = Tk()

        window4.geometry("250x100")

        window4.title('f(x) = ' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c))

        window4.resizable(False, False)

        window4.iconbitmap("calculatrice.ico")

        window4.configure(bg="#fcbf49")

        x = sp.symbols('x')
        f = a*x**2+b*x+c
        derive = sp.diff(f, x)
        derive2 = sp.diff(derive, x)

        title = Label(window4, text="La dérivée seconde est :", bg="#fcbf49")
        der = Label(window4, text=str(derive2), bg="#fcbf49")
        title.grid(column=0, row=0)
        der.grid(column=0, row=1)

    if v1 == 1:

        window2 = Tk()

        window2.geometry("250x100")

        window2.title('f(x) = ' + str(a) + 'x² + ' + str(b) + 'x + ' + str(c))

        window2.resizable(False, False)

        window2.iconbitmap("calculatrice.ico")

        window2.configure(bg="#fcbf49")

        title = Label(window2, text="Les solutions de l'équation f(x)=0 sont :", bg="#fcbf49")
        disx1 = Label(window2, text=x1, bg="#fcbf49")
        disx2 = Label(window2, text=x2, bg="#fcbf49")
        title.grid(column=0, row=0)
        disx1.grid(column=0, row=1)
        disx2.grid(column=0, row=2)

    if v2 == 1:

        x = np.linspace(-10, 10, 400)
        y = a*x**2+b*x+c
        plt.plot(x, y)
        plt.title("Graphique de f(x) = " + str(a) + 'x² + ' + str(b) + 'x + ' + str(c))
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.show()

label = Label(bg="#fcbf49")
label.grid(column=0, row=0)
titlea = Label(window, text="a :", bg="#fcbf49")
titleb = Label(window, text="b :", bg="#fcbf49")
titlec = Label(window, text="c :", bg="#fcbf49")
inta = Entry(window, width=5, )
intb = Entry(window, width=5)
intc = Entry(window, width=5)
titlea.grid(column=0, row=1)
titleb.grid(column=0, row=2)
titlec.grid(column=0, row=3)
inta.grid(column=1, row=1)
intb.grid(column=1, row=2)
intc.grid(column=1, row=3)
label = Label(bg="#fcbf49")
label.grid(column=0, row=4)
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
check1 = Checkbutton(window, text="Solutions", variable=var1, bg="#fcbf49")
check1.grid(column=0, row=5)
check2 = Checkbutton(window, text="Courbe", variable=var2, bg="#fcbf49")
check2.grid(column=0, row=6)
check3 = Checkbutton(window, text="Dérivée", variable=var3, bg="#fcbf49")
check3.grid(column=2, row=5)
check4 = Checkbutton(window, text="Dérivée 2", variable=var4, bg="#fcbf49")
check4.grid(column=2, row=6)
label = Label(bg="#fcbf49")
label.grid(column=0, row=7)
submit=Button(window, text="Valider", command=execute)
submit.grid(column=1, row=8)

window.mainloop()

