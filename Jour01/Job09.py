class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credit = 70
        self.__level = self.__studentEval()

    def get_nom(self):
        return self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom

    def get_numero(self):
        return self.__numero_etudiant

    def get_credit(self):
        return self.__credit
    
    def set_credit(self, credit):
        self.__credit = credit

    def add_credit(self, credit):
        if credit >= 0:
            self.__credit = int(credit)
            return self.__credit
        else:
            print("Ce n'est un entier positif.")

    def __studentEval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80: 
            return "Très bien"
        elif self.__credit >= 70: 
            return "Bien"
        elif self.__credit >= 60: 
            return "Passable"
        elif self.__credit <= 50: 
            return "insuffisant"
        else:
            return False
        
    def studentinfo(self):
        return f'Nom : {self.__nom}\nPrenom : {self.__prenom}\nId : {self.__numero_etudiant}\nNiveau : {self.__level}'

etudiant = Student("Doe", "John", 145)
creds = etudiant.add_credit(30)

print(f"Le nombre de credits de", etudiant.get_nom(), etudiant.get_prenom(), f"est de {creds} credits.")

creds = etudiant.add_credit(70)

print(f"Le nombre de credits de", etudiant.get_nom(), etudiant.get_prenom(), f"est de {creds} credits.")

print(etudiant.studentinfo())
