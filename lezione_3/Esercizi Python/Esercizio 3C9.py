'''Esercizio 3C-9. Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla. 
Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X.
Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."
'''
#esercizio3C9 

x = float(input("Inserisci la coordinata X: "))
y = float(input("Inserisci la coordinata Y: "))

punto = (x, y)

match punto:
    
    case (0, 0):
        print(f"Il punto {punto} si trova nell'origine.")
    
    case (_, 0):
        print(f"Il punto {punto} si trova sull'asse X.")
    
    case (0, _):
        print(f"Il punto {punto} si trova sull'asse Y.")
    
    case (x, y) if x > 0 and y > 0:
        print(f"Il punto {punto} si trova nel primo quadrante.")
    
    case (x, y) if x < 0 and y > 0:
        print(f"Il punto {punto} si trova nel secondo quadrante.")
    
    case (x, y) if x < 0 and y < 0:
        print(f"Il punto {punto} si trova nel terzo quadrante.")
    
    case (x, y) if x > 0 and y < 0:
        print(f"Il punto {punto} si trova nel quarto quadrante.")
    
    case _:
        print("Coordinate non valide.") 