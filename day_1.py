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
    """ merci pour ce first day
    """=
    
    
    """exercice 1: calcul de moyenne"""
a= float(input("entre le premier nombre:"))
b= float(input("entre le second nombre:"))
c= float(input("entre le troisieme nombre:"))
M= (a+b+c)/3
print("la moyenne est:",M)
    


""" exercise:2 conversion celsius en fahrenheit
"""
c= int(input("saisir une temperature en degre celsius"))
F= (9/5)*c+32
print("La tempersture en Farhrenheit est:",F)




""" exercice:3 compter les voyelles d'une chaine de carctere
"""
chaine = input("entrer la chaine;")
voyelles = "aeiuoyAOUIEY"
compteur = 0
for lettre in chaine :
    if lettre in voyelles :
        compteur = compteur +1
print("le nombre de voyelles dans la chaine est : ",compteur) 

 
""" exercice :4 somme des carres
"""
nombre = int(input("saisir un nombre entier positif:"))
while nombre<1 :
    print("error")
    nombre = int(input("kalakala, entre un nombre entier positif:"))
sommes = 0
for i in range(1, nombre+1):
    sommes = sommes+(i*i)
print("la somme des carres de 1 a ",nombre ,"est:",sommes)


""" exercice:5 inverser une chaine de caractere
"""
chaine = input("entrer une chaine de caractere")
inverse = chaine[::-1]
print("la chaine inverse est:",inverse)


""" exercice:6 palindrome
"""
chaine = input("entrer une chaine de caractere")
inverse = chaine[::-1]
if chaine == inverse :
    print("la chaine est un palindrome")
else:
    print("la chaine n'est pas un palindrome")
    
    
    
    
    """ exercice:7 nombre premier
    """
nombre = int(input("entre un nombre entier:"))
if nombre > 1:
    #traitement
    for i in range(2, i+1):
     if nombre % i == 0:
         print(nombre, "n'est pas premier")
         break
     else:
         print(nombre, "est premier")
        
        
else:
    print(nombre, "n'est pas premier")