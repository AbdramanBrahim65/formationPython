def sqrt(nombre):
    racine = nombre ** (1/2)
    print(f"La racine carrée de {nombre} est {racine}")

#donner le paramettre de votre choix a la fonction sqrt
sqrt(4)

#deuxieme methode
from math import sqrt
nombre = int(input("Entrer un nombre : "))
print(sqrt(nombre))