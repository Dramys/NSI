from tkinter import *
import os

window = Tk()

window.geometry("300x160")

window.title("Résolveur d'équation")

window.resizable(False, False)

window.iconbitmap("calculatrice.ico")

window.configure(bg="#fcbf49")

title = Label(window, text="Degré de l'équation :", bg="#fcbf49", font=("Georgia", 12), height=2)
title.pack()

def update_var():
    valeur = value.get()
    return valeur

value = StringVar() 
choix1 = Radiobutton(window, text="1 : f(x)=ax+b", variable=value, value=1, bg="#fcbf49", font=("Georgia", 10), activebackground="#fcbf49", selectcolor="#fcbf49", command=update_var)
choix2 = Radiobutton(window, text="2 : f(x)=ax²+bx+c", variable=value, value=2, bg="#fcbf49", font=("Georgia", 10), activebackground="#fcbf49", selectcolor="#fcbf49", command=update_var)
choix1.pack()
choix2.pack()

def execute():
    valeur = update_var()
    print(valeur)
    if valeur == '1':
        os.system('python premier.py')
    if valeur == '2':
        os.system('python second.py')

label = Label(bg="#fcbf49")
label.pack()    
submit=Button(window, text="Valider", command=execute)
submit.pack()

window.mainloop()