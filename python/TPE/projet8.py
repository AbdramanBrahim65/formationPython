from math import gcd
def decroissant():
    n = int(input("Entrer le nombre max :"))
    liste = []
    for i in range(0,n+10,10):
        liste.append(i)
    liste.sort(reverse=True)
    print("la liste de nombre est ",liste)
decroissant()
def affiche():
    n = int(input("Entrer un nombre :"))
    for n in range(1,n+11):
        print(n)
affiche()
def conversion():
    """shhtyjdt"""
    liste = []
    for i in range(1,301):
        liste.append(i*1.65)
    print(liste)
conversion()

def pgcd():
    a = int(input("Entrer un nombre :"))
    b = int(input("Entrer un nombre :"))
    print(gcd(a,b))
pgcd()

def plusGrand():
    liste = []
    for i in range(0,5):
        n = int(input("Entrer un nombre :"))
        liste.append((i,n))
    min = liste[0][1]
    j=0
    for i in range(0,5):
        if liste[i][1] > min:
            max =liste[i][1]
            j=i
    print(f"le nombre maximale est {max} et son indice est {j}")
plusGrand()
