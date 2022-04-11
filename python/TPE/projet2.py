def acheter_son_billet():
    nombre_billet = int(input("Entrer le nombre de billet : "))
    if nombre_billet >= 1 :
        prix_total = nombre_billet * 25
        print(f"Le prix total de billet est {prix_total} $")
acheter_son_billet()