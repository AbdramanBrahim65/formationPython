class Person:
    def __init__(self,nom):
        self.nom = nom
    def marcher(distance,temp):
        vitesse = distance/temp
        return vitesse


etudiant1 = Person("abdou")
etudiant2 = Person("ali")
etudiant3 = Person("youssouf")
print(etudiant1.nom)
print(etudiant2.nom)
print(etudiant3.nom)
print(Person.marcher(40,4))