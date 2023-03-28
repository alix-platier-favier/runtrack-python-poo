class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def périmètre(self):
        return 2 * (self.longueur) + 2 * (self.largeur)
    
    def surface(self):
        return (self.longueur) * (self.largeur)
    
    def get_longueur(self):
        return self.longueur 
    
    def set_longueur(self, longueur):
        self.longueur = longueur

    def get_largeur(self):
        return self.largeur 
    
    def set_largeur(self, largeur):
        self.largeur = largeur

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur
    
    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    def volume(self):
        return (self.longueur) * (self.largeur) * (self.hauteur)

rectangle = Rectangle(3, 5)
perimetre = rectangle.périmètre()
surface = rectangle.surface()

print("Rectangle:")
print("Périmètre :", perimetre)
print("Surface :", surface)

rectangle.set_longueur(6)
rectangle.set_largeur(10)

print("Nouveau rectangle :")
print("Longueur :", rectangle.get_longueur())
print("Largeur :", rectangle.get_largeur())

paral = Parallélépipède(5, 3, 1)
périmetre = paral.périmètre()
surface = paral.surface()
volume = paral.volume()

paral.set_longueur(10)
paral.set_largeur(6)
paral.set_hauteur(2)

print("Parallélépipède :")
print("Nouvelle longueur :", paral.get_longueur())
print("Nouvelle largeur :", paral.get_largeur())
print("Nouvelle hauteur :", paral.get_hauteur())
