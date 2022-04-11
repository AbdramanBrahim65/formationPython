
def valeurAbsolue():
    a = int(input("Entrer un nombre :"))
    absolue = abs(a)
    return absolue
print("valeur absolue de nombre est ",valeurAbsolue())

def pairImpair():
    a = int(input("Entrer un nombre :"))
    if a % 2 == 0:
        print(f"{a} est pair ")
    else:
        print(f"{a} est impair ")
pairImpair()
def max():
    a = input("Entrer un nombre :")
    b = input("Entrer un nombre :")
    if a > b:
        print(a)
    else :
        print(b)
    
max()
def moyenne():

    moyenne = int(input("Entrer votre moyenne :"))
    if moyenne >=10:
        print("Vous êtes reussi !")
    else:
        print("Non reussi !")
moyenne()

def etatEau():
    T = int(input("Entrer un nombre :"))
    if T <= 0:
        print("c'est la glace ")
    elif T> 100:
        print("c'est de la vapeur")
    else:
        print("c'est du liquide")
etatEau()