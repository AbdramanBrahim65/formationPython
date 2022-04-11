def dico(n):
    dictionnaire = {}
    for i in range(n):
        cle = input("entrer la clé : ")
        valeur = input("entrer la valeur : ")
        dictionnaire[cle] = valeur
    print(dictionnaire)
#dico(5)
def afficheDico():
    dico = {'1':1,'2':2,'3':3}
    items = dico.items()
    for key ,value in items:
        print(f'({key},{value})')
afficheDico()