#esercizio8-12

def make_sandwich(*items):
    
    print("Making a sandwich with the following items:")
    
    for item in items:
    
        print(f"-{item}")
    print("Your sandwich is ready!")

make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "avocado")
make_sandwich("peanut butter", "jelly")