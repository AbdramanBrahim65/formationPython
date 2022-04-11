def possibilite(classe = "second_classe"):
    classe = input("Entrer la classe souhaité : ")
    if classe == "premier_classe":
        print("Vous aurez votre repas ! ")
    elif  classe == "second_classe":
        print("Vous n'aurez pas un repas ! ")
possibilite()
