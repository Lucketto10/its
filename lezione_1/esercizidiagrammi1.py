#esercizidiagrammi1

a : int = int(input("Inserisci a: "))
b : int = int(input("Inserisci b: "))

if a > b:
    
    c: float = (a**2 - b**2) ** (1/2)

    print(f"C'è: {c}")

else:
    print("Errore")
    