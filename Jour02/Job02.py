class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        return self.age
    
    def bonjour(self):
        return "hello"
    
    def modifierAge(self, N_age):
        self.age = N_age

class Eleve(Personne):
    def allerenCours(self):
        return "Je vais en cours"
    
    def affichageAge(self):
        return "J'ai {} ans.".format(self.age)
    
class Professeur(Personne):
    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        return "Le cours va commencer"
    
personne = Personne()
eleve = Eleve()
professeur = Professeur("Art Plastique")

print(personne.bonjour())
print(eleve.allerenCours())
eleve.modifierAge(15)
print(eleve.affichageAge())

professeur.modifierAge(40)
print(professeur.bonjour())
print(professeur.enseigner())