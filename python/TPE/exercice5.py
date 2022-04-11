choix = True
while choix is not False :
    print("================================================")
    print("1--Pour continuer : ")
    print(" Tout les autres nombres pour s'aareter : ")
    nombreEssaye = int(input("entre un nombre : "))
    nombreCoupe = int(input("Entrer le nombre de coupe du monde de France : "))
    if nombreEssaye == 1:
        if nombreCoupe == 2:
            print("Bravo! vous avez gagné ")
        else:
            print("Essayé un autre fois ")
    else :
        print("Merci pour la confiance")
        choix = False