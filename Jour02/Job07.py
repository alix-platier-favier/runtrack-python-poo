import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu(Carte):
    def __init__(self):
        self.paquet = []
        couleurs = ["Pique", "Coeur", "Trèfle", "Carreau"]
        valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.choice(self.paquet)

    def donner_carte(self):
        return self.paquet.pop()
    
class Joueur(Carte):
    def __init__(self):
        self.score = 0
        self.main = []

    def pioche(self, carte):
        self.main.append(carte)
        if carte.valeur == "As":
            if self.score + 11 <= 21:
                self.score += 11
            else:
                self.score += 1
        elif carte.valeur == ["Valet", "Dame", "Roi"]:
            self.score += 10
        else:
            self.score += carte.valeur

                