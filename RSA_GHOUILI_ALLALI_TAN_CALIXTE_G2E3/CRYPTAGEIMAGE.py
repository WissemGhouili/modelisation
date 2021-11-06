#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:50:13 2021

@author: g20014195
"""

import random


def est_Premier(nb):
    i = 2
    while(i < nb):
        if nb%i == 0:
            return False
        else:
            i += 1
    return True


def genereNbPremierEntre(x, y):
    
    listeNbPremier = []
    
    for i in range(x, y):
        for nb in range(2, i):
            if est_Premier(nb) == True :
                listeNbPremier.append(nb)

    NbPremierAleatoire = random.choice(listeNbPremier)
    return NbPremierAleatoire
        

def pgcd(a,b):
    if b==0:
        return a
    else:
        reste=a%b
        return pgcd(b,reste)
    
    
def euclide(a,b, Reste, Quotient):
    if b==0:
        return a
    else:
        r=a%b
        q = a//b
        Reste.append(a)
        Quotient.append(q)
        euclide(b,r, Reste, Quotient)

    return Reste, Quotient




def euclideEtendu(a, b, Reste, Quotient):
    
    a = Reste[1]
    u = 1
    b = Reste[0]
    v = (-1)
    constT = 1
    
  

    
    for i in range(len(Reste)):
        b = a
        a = Reste[i]
        tmpU = u
        u = v
        v = -Quotient[i] * v + tmpU
        constT = 1
 
    
    while (u < 0):
        u = u + b;
        v = v - a;
    
    while (u > b):
        u = u - b;
        v = v + a;
   
  
    if (constT  == (a*u) + (b*v)):
        print("Génération des clées réussis \n")
    else :
        print("Echec de la génération des clées réussis\n")

    return u
    


q = 61

p = 47
   
if q < p :
        tmpQ = q
        q = p
        p = tmpQ

print("P est égal à %d"%p)
print("Q est égal à %d"%q)

n = p * q;
print("N est égal au produit de p et q :", n);

fi = (p - 1) * (q - 1);
print("ϕ est égal à :", fi);


Reste=[]
Quotient=[]

d = genereNbPremierEntre(255, 400)
while True:
    if pgcd(d, fi) != 1:
        genereNbPremierEntre(255, 400)
    else:
        break
print("On choisit le nombre premier 'd' qui est égale à", d, "premier avec 'ϕ'");

euclide(d, fi, Reste, Quotient)


Reste.reverse()
Quotient.reverse()



e = euclideEtendu(d, fi, Reste, Quotient)

clePublique = (n, d)
clePrive = (n, e)
print("Clé publique:", clePublique)
print("Clé privé:", clePrive)



#Transformation image en matrice


from PIL import Image
import numpy as np


img = Image.open("image.jpg")
img.show()

x=200
y=200

image = np.array(img.resize((x,y)))


print("Matrice de l'image", image)


Cryptage = []

for i in range(x):
    for j in range (y):
        for k in range(3):
            px = int(image[i][j][k])
            px = (px ** d) % n
            Cryptage.append(px)
            
            if px > 255:
                px = px%256
                
            image[i][j][k] = px
            
print("Cryptage de l'image reussis \n")
Image.fromarray(image).save("image_crypte.jpg")
Image_crypte = Image.open("image_crypte.jpg")
Image_crypte.show()


p = 0
print("Décryptage de l'image en cours, cela peut prendre quelque secondes \n")
for i in range(x):
    for j in range (y):
        for k in range(3):
            px = Cryptage[p] 
            px = (px ** e) % n
            image[i][j][k] = px
            p = p+1
                        
print("Décryptage reussis \n")
print("Matrice image décrypté :", image)          
Image.fromarray(image).save("image_decrypte.jpg")
Image_decrypt = Image.open("image_decrypte.jpg")
Image_decrypt.show()
