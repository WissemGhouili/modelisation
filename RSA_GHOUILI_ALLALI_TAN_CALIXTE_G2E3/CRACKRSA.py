#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:27:38 2021

@author: g20014195
"""

def decompose (n): 
    i=2
    Facteur=[]
    while n>1: 
        while n%i==0: 
            Facteur.append(i)
            n=n/i
        i=i+1
    
    return Facteur

        
def est_Premier(nb):
    i = 2
    while(i < nb):
        if nb%i == 0:
            return False
        else:
            i += 1
    return True
        

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
    
    print("Initialisation :\n",constT  ,"=", a, "*" ,u ,"+", b ,"*", v)
    

    
    for i in range(len(Reste)):
        b = a
        a = Reste[i]
        tmpU = u
        u = v
        v = -Quotient[i] * v + tmpU
        constT = 1
        print(constT ,"=", a, "*" ,u ,"+", b ,"*", v)
    
    while (u < 0):
        u = u + b;
        v = v - a;
    
    while (u > b):
        u = u - b;
        v = v + a;
   
    print(constT  ,"=", a, "*" ,u ,"+", b ,"*", v)
    if (constT  == (a*u) + (b*v)):
        print("Vérification égalité : OK \n")
    else :
        print("Vérification égalité : ERREUR \n")
    
    print("Inverse modulaire de d modulo N :")
    print(a, '*', u, '≡', 1, '[', b, ']', '\n')
    
    return u

def decrypte(ContenuCrypte, e, n):
    ListTemp=[]
    for i in range(len(ContenuCrypte)):
        i = ContenuCrypte[i]
        i = (i ** e) % n
        i = chr(i)
        ListTemp.append(i)
        
    mot = ""    
    for i in range(len(ListTemp)):
        mot += ListTemp[i]
    return mot



    
messageCrypté = [498, 484, 58, 404, 660, 221, 404, 545, 101, 86, 86, 221, 404, 116, 404, 101, 184, 757, 336, 221, 611, 253]
n = 899
d = 59
cléPublique = (n, d)
print("On récupere la clé Publique qui est :", cléPublique, '\n', "Nous arrivons à intercepter un message crypté entre Alice et Bob qui est : \n", messageCrypté, '\n')


#DEBUT DE L'ATTAQUE
print("Debut de l'attaque \n")

DecompositionN = decompose(n)
p = DecompositionN[0]
q = DecompositionN[1]
print("On décompose N et on obtient ainsi p et q : ", "%d ="%n, p, '*', q, '\n')

fi = (p - 1) * (q - 1)
print("NOus recalculons ϕ avec p et q :", fi, '\n')

print("Enfin nous recalculons e à l'aide de d et de ϕ")

Reste=[]
Quotient=[]
euclide(d, fi, Reste, Quotient)
Reste.reverse()
Quotient.reverse()
e = euclideEtendu(d, fi, Reste, Quotient)

clePrive = (n, e)
print("De ce fait, on obtient la clé privée:", clePrive, "qui va nous permettre de déchiffré le message chiffré")


messageDecrypt = decrypte(messageCrypté, e, n)
print("En le décryptant avec la clé privée nous obtenons le message entre Alice et bob qui est", '"', messageDecrypt, '"')