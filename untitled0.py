# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 21:48:45 2022

@author: pc
"""
class Compte:
    def __int__(self,nom,prenom):
        self.nom=nom
        self.prenom=prenom
    def affiche (self):
        return "nom",self.nom,"prenom",self.prenom
B=Compte("luc","jean")
print(B.affiche)