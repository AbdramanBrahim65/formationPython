def addition(a,b):
    """return add of two numbers"""
    return a+b
def soustraction(a,b):
    """return add of two numbers"""
    return a-b
def multiplication(a,b):
    return a*b
def divisionDecimale(a,b):
    #Structure ternaire
    if b != 0:
        return a/b
    else:
        return "Impossible de diviser un nombre par zero!"
def divisionEntiere(a,b):
    if b!= 0:
        return a//b
    else:
        return "Impossible de diviser un nombre par zero!"
def modulo(a,b):
    return a%b
def puissance(a,b):
    return a**b

def main(a,b):
    print("=========Menu===========")
    print(" 1 - pour l'addition ")
    print(" 2 - pour la soustraction ")
    print(" 3 - pour la multiplication ")
    print(" 4 - pour la divisionDecimal ")
    print(" 5 - pour la divisionEntiere ")
    print(" 6 - pour le modulo ")
    print(" 7 - pour la puissance ")
    print(" 8- Voulez-vous quitter ")
    print("==============================")
    quand = True
    while quand is not False:
        choice = int(input(" Entrer votre choix : "))
        if choice == 1:
            print(addition(a,b))
        elif choice == 2:
            print(soustraction(a,b))
        elif choice == 3:
            print(multiplication(a,b))
        elif choice == 4:
            print(divisionDecimale(a,b))
        elif choice == 5:
            print(divisionEntiere(a,b))
        elif choice == 6:
            print(modulo(a,b))
        elif choice  == 7:
            print(puissance(a,b))
        elif choice == 8:
            quand = False
            print("Merci d'avoir essayé !")
        else:
            print("vraiment vous ne voulez pas essayé ? ")
            print("sinon tapez 1 :")
            essaye = int(input("Entrer un nombre de choix pour continuer : "))
            if essaye == 1:
                quand = True
            else :
                quand = False
                print("Merci d'avoir essayé !")
if __name__=='__main__':
number_1 = int(input("Entrer un nombre : "))
number_2 = int(input("Entrer un nombre : "))
main(number_1,number_2)


        