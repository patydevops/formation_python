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
    """
    
    
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
    
    
""" exercice:8 Somme
"""
a= float(input("entre le premier nombre:"))
b= float(input("entre le second nombre:"))
S= a+b
print('la somme de ces nombres est:',S)


""" exercice:9 Le Tri des visteurs
"""
age=int(input("entre ton age:"))
if age >= 18:
  print("Majeur") 
else:
  print("Mineur")  
    
  
""" exercice:10 Mes Diviseurs
"""    
nombre = int(input("entre un nombre entier:"))
while nombre <= 0:
    print("error")
    nombre = int(input("entre un nombre entier:"))
print("les diviseurs de ce nombre sont:")
for i in range(1, nombre+1):
 if nombre % i == 0:
    print(i)
    

""" exercice:10 Le PGCD
"""          
x= int(input("entre le premier nombre entier:"))
y= int(input("entre le second nombre entier:"))
while x <= 0:
     print("error")
     x = int(input("entre le premier nombre entier:"))
while y <= 0:
     print("error")
     y = int(input("entre le second nombre entier:"))    
if x > y :
    min = y
else :
    min = x
for i in range (1, min+1):
       if x % i == 0 and y % i == 0:
           pgcd = i
print("le pgcd de ces deux nombres est:", pgcd)    
    
    
""" exercice:11 Le Tri
"""    
nombres= input("saisir une liste de nombres:")
liste=[int(nombre)for nombre in nombres.split()]
print(liste)
trie=sorted(liste)
print(trie)


""" exercice:12 Annee bissextile
"""     
annee= int(input("saisir votre annee:"))
if annee % 4 == 0 and (annee % 100 != 0 or annee % 400 == 0):
    print(annee, "est bissextile")
else:
    print(annee, "n'est pas bissextile")
    
 
""" exercice:13 Mon occurence
""" 
chaine= input("saisissez une chaine de caractere:")
matrice= {}
for caractere in chaine:
    if caractere in matrice:
        matrice[caractere]+=1
    else:
        matrice[caractere]=1
for caractere,occurence in matrice.items():
    print(caractere+"-"+ str(occurence))
        
    


