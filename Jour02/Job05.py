import math

class Forme:
    def aire(self):
        return 0

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * (self.radius) ** 2


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur
    
rectangle = Rectangle(3, 4)
cercle = Cercle(2)

print(rectangle.aire())
print(cercle.aire())