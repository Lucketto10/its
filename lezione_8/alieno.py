class Alieno:

    def __init__(self,galaxy):
        self.setGalaxy(galaxy)

    def setGalaxy(self,galaxy): 
        if galaxy :

            self.galaxy = galaxy 

        else : 
            print(f" errore la galassia di provenienza nn può essere una stringa vuota ")

    def getgalaxy(self) : 
        return self.galaxy 
    
    def speak(self) : 
        print(f"\n faoivnronfioen \n")

    def __str__(self):
        return f"\n alieno proveniente dalla galassia {self.getgalaxy()}!\n"