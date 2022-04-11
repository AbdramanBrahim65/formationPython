import TPE.calculatrice
from TPE.calculatrice import *

def affichage():
    print(f" C'est la puissance de 14 par 2 : {TPE.calculatrice.puissance(14,2)}")

    #Deuxieme manière d'ecrire


    print("c'est l'addtion de 14 et 2 : {}".format(addition(14,2)))


    #Troisiéme manière d'écrire 

    print("C'est la soustraction de 14 et 2 : ",soustraction(14,2))
affichage()