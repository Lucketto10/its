from persona import Persona

class studente(Persona) : 

    def __init__(self, name, lastname, age, matricola):
        super().__init__(name,lastname,age)
        self.setmatricola(matricola)

    def setmatricola(self, matricola):

        if matricola : 
            self.matricola = matricola

        else : 
            print(f"la matrice non può essere vuota")

    def getmatricola(self) : 

        return self.matricola
    
    def __str__(self):
        return f"\nNome: {self.getName()} \nCognome {self.getLastname()}\nMatricola {self.getmatricola()} "