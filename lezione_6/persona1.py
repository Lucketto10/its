#persona1.py

class Persona:

   #costruttore 
    def __init__(self, name = str, lastname = str, age = int):

        self.name = name
        self.lastname = lastname
        self.age = age

    #funzione della classe Persona che visualizza in input i dati di una perosna
    def displayData(self)  ->  None:
        print(f"Nome: {self.name}\n cognome: {self.lastname}\n età: {self.age}")