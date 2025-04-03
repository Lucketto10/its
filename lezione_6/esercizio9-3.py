class User:
    
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name  
        self.last_name = last_name    
        self.age = age                            
        self.location = location      

    def describe_user(self):
        print(f"Nome: {self.first_name} {self.last_name}")
        print(f"Età: {self.age}")
        print(f"Posizione: {self.location}")

    def greet_user(self):
        print(f"Ciao, {self.first_name}! Benvenuto nel nostro sistema.")

user1 = User("Diego", "Laghetti", 18, "Milano")
user2 = User("Luca", "Taggiasco", 19, "Roma")
user3 = User("Mario", "Verdi", 22,  "Napoli")

user1.describe_user()
user1.greet_user()

print() 

user2.describe_user()
user2.greet_user()

print()

user3.describe_user()
user3.greet_user()
