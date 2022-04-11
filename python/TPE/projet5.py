from math import pi
def somme():
    a=int(input("Entrer a :"))
    b=int(input("Entrer b :"))
    c=int(input("Entrer b :"))
    print(f"la somme de trois nombre est {a+b+c}")
somme()

def volumeCone():
    rayon = float(input("Entrer le rayon de la cône :"))
    hauter = int(input("Entrer la hauter de la cone :"))
    volume = (pi * (rayon**2)*hauter)/3
    print("le volume de la cône est ",volume)
volumeCone()

def indiceMasse():
    poids = float(input("Entrer votre poids svp :"))
    taille = float(input("Entrer votre taille svp :"))
    imc = poids / (taille**2)
    return imc
print("votre indice de masse corporelle est ",indiceMasse())
