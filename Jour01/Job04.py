class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return "Je suis" + " " + self.nom + " " + self.prenom
    
personneA = Personne('John', 'Doe')
personneB = Personne('Jean', 'Dupon')

print(personneA.SePresenter())
print(personneB.SePresenter())