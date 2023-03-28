class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_pages(self):
        return self.__pages
    
    def set_pages(self, pages):
        if pages >= 0:
            self.__pages = int(pages)
        else:
            print("Le nombre n'est pas valide.")

    def get_disponible(self):
        return self.__disponible
    
    def set_disponible(self, disponible):
        self.__disponible = disponible

    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False

    def emprunter(self):
        if self.verification() == True:
            return True
        else:
            return False
        
    def rendre(self):
        if self.emprunter() == True:
            return False
        else:
            return True


livre = Livre("H2G2", "Douglas Adams", 224)

print("Titre:", livre.get_auteur())
print("Auteur:", livre.get_titre())
print("Nombre de pages:", livre.get_pages())
print("Disponibilité :", livre.verification())
print("Empruntable :", livre.emprunter())
print("Rendable :", livre.rendre())

livre.set_disponible(False)
print("Nouvelle disponibilité :", livre.get_disponible())