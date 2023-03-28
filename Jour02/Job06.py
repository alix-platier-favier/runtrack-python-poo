class Vehicule:
    def __init__(self, marque, année, modèle, prix):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix

    def InformationsVehicule(self):
        return f"Marque: {self.marque}\nModèle: {self.modèle}\nAnnée: {self.année}\nPrix du véhicule: {self.prix}"
    
    def demarrer(self):
        return "Attention, je roule."
    
class Voiture(Vehicule):
    def __init__(self, marque, année, modèle, prix, portes):
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix
        self.portes = portes

    def InformationsVehicule(self):
        return f"Marque: {self.marque}\nModèle: {self.modèle}\nPortes: {self.portes}\nAnnée: {self.année}\nPrix du véhicule: {self.prix} €"
    
    def demarrer(self):
        return "Attention, je drift."
    
class Moto(Vehicule):
    def __init__(self, marque, année, modèle, prix, roue):
        self.roue = roue
        self.marque = marque
        self.modèle = modèle
        self.année = année
        self.prix = prix


    def InformationsVehicule(self):
        return f"Marque: {self.marque}\nModèle: {self.modèle}\nRoues: {self.roue}\nAnnée: {self.année}\nPrix du véhicule: {self.prix} €"

    def demarrer(self):
        return "Attention, je wheelie."
    
vroom = Voiture("Peugeot", "205 CTI 1.6", "4", "1988", "23900")
roues = Moto("Yamaha", "1200 Vmax", "2", "1987", "4500")

print("VOITURE :")
print(vroom.InformationsVehicule())
print(vroom.demarrer())
print("MOTO :")
print(roues.InformationsVehicule())
print(roues.demarrer())