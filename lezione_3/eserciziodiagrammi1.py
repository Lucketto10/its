#eserciziodiagrammi1

liberi = int(input("Inserire il numero di posti liberi: "))
occupati= 0
posti = liberi

while True:
    opzione = str(input("Inserisci opzione: "))
    
    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
                occupati += 1
    
            else:
                print("Non ci sono posti disponibili")
    
        case "uscita":
    
            if liberi < posti:
                liberi += 1
    
            else:
                print("Tutti i posti sono già disponibili")
    
        case "stato":
            print("liberi", liberi)
            print("occupati", occupati)
    
        case "esci":
    
            break
    
        case _:
    
            continue