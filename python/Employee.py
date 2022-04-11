from datetime import date
class Employe:
    def __init__(self,matricule,nom,prenom,date_naissance,date_embauche,salaire):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.date_embauche = date_embauche
        self.salaire = salaire
    def age_employe(self,age):
        return age 
   #def anciennete(self):
     #self.annee = date - self.date_embauche
       # return annee
    #def augmentation_salaire(self,augmentation):
        #if self.annee < 5 :
            #self.augmentation = 0.02
           # salaire = salaire + augmentation
            #return salaire
        #elif self.annee < 10 :
            #self.augmentation = 0.05
           # salaire = salaire + augmentation
           # return salaire
       # else:
          #  self.augmentation = 0.1
           # salaire = salaire + augmentation
           # return salaire
    def affiche_employee(self):
        print("le matricule de l'employé est : ",self.matricule)
        print("le nom de l'employé est : "+self.nom.upper() +" "+self.prenom.capitalize())
        print("le age de l'employé est : ",self.age_employe(14))
        print("l'ancienneté de l'employé est : ",self.date_naissance)
        print("la date d'embauche  de l'employé est : ",self.date_embauche)
        print(f"la salaire  de l'employé est : {self.salaire}$")

    
  
    





