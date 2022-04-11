def argent():
    sommeTotal = int(input("Entrer la somme totale qqu'il souhaite placer : "))
    nombreAnnee = int(input("Entrer le nombre d'annee pandant lequelles il souhaite placer son argent :"))
    tauxIntêret = float(input("Entrer le taux d'intêret auquel il a accés : "))
    if sommeTotal < 0 and nombreAnnee < 0 and tauxIntêret <0 :
        print("Svp les nombres ne sont negatifs !")
    else:
        interet = sommeTotal * nombreAnnee * tauxIntêret
        print("l'interet est : ",interet)
argent()
        