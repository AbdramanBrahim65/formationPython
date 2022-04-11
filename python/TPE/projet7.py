def motDePasse():
    mot_passe = input("Entrer votre de passe : ")
    choix = True
    while choix is not False :
        print("================================================")
        print("1--Pour continuer : ")
        print(" Tout les autres nombres pour s'aareter : ")
        nombreEssaye = int(input("entre un nombre : "))
        if nombreEssaye == 1:
            if mot_passe == "Admin":
                print("Connexion reussie ")
            else :
                print("Connexion echoué ")
            choix =False
        else :
            print("Merci pour la confiance")
            choix = False
motDePasse()

def sommeCarre():
    n = int(input("Entrer la taille de votre somme : "))
    somme = 0
    for i in range(1,n+1):
        somme = somme +  i**2
    print("la somme de carrée de nombre est ",somme)
sommeCarre()