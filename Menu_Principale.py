import tkinter as tk
from datetime import datetime
from subprocess import call
from tkinter import *
from tkinter import ttk
from  cProfile import  label
from  tkinter import  messagebox



def client():

        root.destroy()
        call(["python","Client.py"])


def produit():

        root.destroy()
        call(["python","Liste_Produit.py"])




root = Tk()
root.title("Connexion")
root.geometry("700x400+450+200")
root.resizable(False, False)
root.configure(background="#091821")

#Ajouter le titre

lbltitre=Label(root,borderwidth=3, relief=SUNKEN, text="MENU PRINCIPAL", font=("Sans Serif", 25), background="#2F4F4F",fg="white")
lbltitre.place(x=0,y=0, width=700)

lbltext=Label(root,  text="Sur la vente de poulets", font=("Sans Serif", 25), fg="white",bg="#091821",)
lbltext.place(x=0,y=50, width=700)


#Liste de Produit
btnproduit=Button(root,text="CLIENT",font=("Arial",16),bg="#02691E",fg="white",borderwidth=3,command=client)
btnproduit.place(x=10,y=190, width=200,height=50)

#Etiquette
btnEtiquette=Button(root,text="Etiquette",font=("Arial",16),bg="#02691E",fg="white",borderwidth=3)
btnEtiquette.place(x=250,y=190, width=200,height=50)

#Produit
btnproduit=Button(root,text="Produit",font=("Arial",16),bg="#02691E",fg="white",borderwidth=3, command=produit)
btnproduit.place(x=490,y=190, width=200,height=50)

#afficher notre interface graphique
root.mainloop()