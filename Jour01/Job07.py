class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

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

livre = Livre("H2G2", "Douglas Adams", 224)

print("Titre:", livre.get_auteur())
print("Auteur:", livre.get_titre())
print("Nombre de pages:", livre.get_pages())

livre.set_pages(224.5)
livre.set_pages(250)


print("Nombre de pages:", livre.get_pages())
