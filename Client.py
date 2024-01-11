import tkinter as tk
from datetime import datetime
from subprocess import call
from tkinter import *
from tkinter import ttk
from cProfile import label
from tkinter import messagebox
import mysql.connector


# cd C:\Users\pc\AppData\Local\Programs\Python\Python310
# python -m pip install mysql.connector=python

def Ajouter():
    matricule = txtmatricule.get()
    nom = txtnom.get()
    produitprit=txtproduit.get()
    quantite=txtQuantite.get()
    tel = txttelephone.get()
    age = txtage.get()
    sexe = valeurSexe.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_poulet")
    meConnecte = maBase.cursor()

    try:
        sql = "INSERT INTO clients(Matricule,Nom,Age,Tel,Quantite,ProduitPrit,Sexe) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (matricule, nom, tel, age, quantite, produitprit, sexe)
        meConnecte.execute(sql, val)
        maBase.commit()
        dernierNumero = meConnecte.lastrowid
        messagebox.showinfo("information", "Client ajouter")
        root.destroy()
        call(["python", "Client.py"])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()


def Modifier():
    nom = txtnom.get()
    tel = txttelephone.get()
    age = txtage.get()
    quantite=txtQuantite.get()
    produitprit = txtproduit.get()
    sexe = valeurSexe.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_poulet")
    meConnecte = maBase.cursor()

    try:
        sql = "update clients set Nom= %s,Tel= %s,Age= %s,Quantite= %s,ProduitPrit= %s,Sexe= %s where Matricule= %s"
        val = (nom, tel, age, produitprit,quantite,sexe)
        meConnecte.execute(sql, val)
        maBase.commit()
        dernierNumero = meConnecte.lastrowid
        messagebox.showinfo("information", "Client modifier")
        root.destroy()
        call(["python", "Client.py"])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()


def Supprimer():
    matricule = txtmatricule.get()

    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_poulet")
    meConnecte = maBase.cursor()

    try:
        sql = "delete from clients  where Matricule= %s"
        val = (matricule,)
        meConnecte.execute(sql, val)
        maBase.commit()
        dernierNumero = meConnecte.lastrowid
        messagebox.showinfo("information", "Client  supprimer")
        root.destroy()
        call(["python", "Client.py"])

    except Exception as e:
        print(e)
        maBase.rollback()
        maBase.close()


root = Tk()
root.title("Vente des poulets")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#091821")

# titre
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="FORMULAIRE DES PROFFESSEURS", font=("Arial", 25),
                 background="#2F4F4F", fg="#FFFAFA")
lbltitre.place(x=0, y=9, width=1350, height=100)

# id vente
lbllmatricule = Label(root, text="Matricule:",
                    font=("Arial", 18), bg="#091821", fg="white")
lbllmatricule.place(x=90, y=150, width=150)
txtmatricule = Entry(root, bd=4, font=("Arial", 13))
txtmatricule.place(x=250, y=150, width=200)

lbllnom = Label(root, text="Nom:",
                    font=("Arial", 18), bg="#091821", fg="white")
lbllnom.place(x=90, y=200, width=150)
txtnom = Entry(root, bd=4, font=("Arial", 13))
txtnom.place(x=250, y=200, width=200)

# nom produit
lbllproduit = Label(root, text="Produit pris :",
                      font=("Arial", 18), bg="#091821", fg="white")
lbllproduit.place(x=90, y=250, width=150)
txtproduit= Entry(root, bd=4, font=("Arial", 13))
txtproduit.place(x=250, y=250, width=200)



# quantite
lbllQuantite = Label(root, text="Quantité_produit :",
                     font=("Arial", 18), bg="#091821", fg="white")
lbllQuantite.place(x=90, y=300, width=150)
txtQuantite = Entry(root, bd=4, font=("Arial", 14))
txtQuantite.place(x=250, y=300, width=200)

# Nombre de kilo
lbllage = Label(root, text="Age:",
                     font=("Arial", 18), bg="#091821", fg="white")
lbllage.place(x=70, y=350, width=150)
txtage = Entry(root, bd=4, font=("Arial", 14))
txtage.place(x=250, y=350, width=200)

# telephone
lblltelephone = Label(root, text="Telephone:",
                     font=("Arial", 18), bg="#091821", fg="white")
lblltelephone.place(x=70, y=400, width=150)
txttelephone = Entry(root, bd=4, font=("Arial", 14))
txttelephone.place(x=250, y=400, width=200)


# sexe
valeurSexe = StringVar()
lblsexe = Label(root, text="Sexe :",
                font=("Arial", 18), bg="#091821", fg="white")
lblsexe.place(x=105, y=450, width=150)
lblSexeMasculin = Radiobutton(root, text="Mall", value="M", variable=valeurSexe, indicatoron=0, font=("Arial", 18),
                              bg="#091821", fg="#696969")
lblSexeMasculin.place(x=250, y=450, width=130)
lblSexeFeminin = Radiobutton(root, text="Femelle", value="F", variable=valeurSexe, indicatoron=0, font=("Arial", 18),
                             bg="#091821", fg="#696969")
lblSexeFeminin.place(x=400, y=450, width=130)

# Enregsitrer
btnAjouter = Button(root, text="Ajouter", font=("Arial", 16), bg="#02691E", fg="white", command=Ajouter)
btnAjouter.place(x=250, y=500, width=200)

# Modifier
btnmodifier = Button(root, text="Modifier", font=("Arial", 16), bg="#02691E", fg="white", command=Modifier)
btnmodifier.place(x=250, y=550, width=200)

# supprimer
btnsupprimer = Button(root, text="Supprimer", font=("Arial", 16), bg="#02691E", fg="white", command=Supprimer)
btnsupprimer.place(x=250, y=600, width=200)

# table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6,7,), height=2, show="headings")
table.place(x=540, y=150, width=790, height=450)

# Entete
table.heading(1, text="Matricule")
table.heading(2, text="Nom")
table.heading(3, text=" Tel")
table.heading(4, text=" Age")
table.heading(5, text="ProduitPrit")
table.heading(6, text="Quantité_produit")
table.heading(7, text="Sexe")

# Modifier les dimensions des colonnes
table.column(1, width=50)
table.column(2, width=50)
table.column(3, width=50)
table.column(4, width=100)
table.column(5, width=50)
table.column(6, width=50)
table.column(7, width=50)


# afficher les informations de la table
maBase = mysql.connector.connect(host="localhost", user="root", password="", database="gestion_poulet")
meConnecte = maBase.cursor()
meConnecte.execute("select * from clients")
for row in meConnecte:
    table.insert('', END, value=row)
maBase.close()

# afficher notre interface graphique
root.mainloop()
