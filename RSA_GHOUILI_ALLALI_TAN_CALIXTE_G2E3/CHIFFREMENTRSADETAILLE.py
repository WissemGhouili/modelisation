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
   
    print(constT  ,"==", a, "*" ,u ,"+", b ,"*", v)
    if (constT  == (a*u) + (b*v)):
        print("Vérification égalité : OK \n")
    else :
        print("Vérification égalité : ERREUR \n")
    
    print("Inverse modulaire de d modulo N :")
    print(a, '*', u, '≡', 1, '[', b, ']', '\n')
    
    return u
    

              

    
while True:
    print("Choisissez un nombre premier 'q'");
    q = abs(int(input()));
    if est_Premier(q) == False :
        print("Ce n'est pas un nombre premier ou un nombre positif, réessayez");
    else:
        break;

while True:
    print("Choisissez un nombre premier 'p'");
    p = abs(int(input()));
    if est_Premier(p) == False :
        print("Ce n'est pas un nombre premier ou un nombre positif, réessayez");
    else:
        break;

   


n = p * q;
print("N est égal au produit de p et q :", n);

fi = (p - 1) * (q - 1);
print("ϕ est égal à :", fi);


Reste=[]
Quotient=[]


d = genereNbPremierEntre(100, 400)
while True:
    if pgcd(d, fi) != 1:
        genereNbPremierEntre(100, 400)
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



#DEMONSTRATION DE CRYPTAGE ET DECRYPTAGE D'UN MESSAGE

message = input("Entrer un message: \n")
message = message.lower()

ContenuCrypte = []

def crypte(message, ContenuCrypte):
    for i in range(len(message)):
        i = message[i]
        i = ord(i)
        i = (i ** d) % n
        ContenuCrypte.append(i)
    return ContenuCrypte

crypte(message, ContenuCrypte)
print("Apres le cryptage :", ContenuCrypte)



def decrypte(ContenuCrypte):
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

messageDecrypt = decrypte(ContenuCrypte)
print("Le message décryptée est : ", messageDecrypt)