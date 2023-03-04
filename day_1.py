# -*- coding: utf-8 -*-=

"""
Spyder Editor

This is a temporary script file.
"""
""" exo2: ecrire un program qui permet de donner l'etat d'un nombre sachant qu'un nombre 
a 3 etats (negatif neutre et positif)
"""
a= float(input("entrer le nombre:"))
if (a<0):
    print ("le nombre est negatif")
if (a==0):
    print ("le nombre est neutre")
if (a>0):
    print ("le nombre est positif")
    

nombre = int(input("Entrez un entier positif :"))
while (nombre<1):
    print ("error")
    nombre = int(input("Entrez un entier positif s'il vous plait:"))
if nombre%2==0:
    print(nombre, " est pair.")
else:
    print(nombre, " est impair.")