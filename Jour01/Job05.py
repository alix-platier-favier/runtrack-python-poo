class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1  
        return self.age
    
    def nommer(self, prenom):
        self.prenom = prenom
        return self.prenom

animal1 = Animal()
print(f"L'age de l'animal est {animal1.vieillir()}")
print(f"L'animal se nomme {animal1.nommer('Luna')}")




