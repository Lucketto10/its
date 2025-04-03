class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def setLegs(self, legs):
        self.legs = legs

    def getLegs(self):
        return self.legs

    def printInfo(self):
        print(f"Name: {self.name}, Legs: {self.legs}")

dog = Animal("Dog", 4)
cat = Animal("Cat", 4)

print(dog.name)  
print(cat.name)  

dog.legs = 3
print(dog.legs)  

dog.setLegs(5)
print(dog.legs)  

print(dog.getLegs())  

dog.printInfo()  
cat.printInfo()  
