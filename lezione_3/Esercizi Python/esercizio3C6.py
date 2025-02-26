#esercizio3C6 

animale = input("Digita il nome di un animale: ")
habitat = input(f"Digita l'habitat in cui vive l'animale {animale}: ")

animal_type = "unknown"

match animale:
    
    case animale if animale in ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]:
        animal_type = "Mammiferi"
        print(f"{animale} appartiene alla categoria dei {animal_type}!")
    
    case animale if animale in ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        animal_type = "Rettili"
        print(f"{animale} appartiene alla categoria dei {animal_type}!")
    
    case animale if animale in ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]:
        animal_type = "Uccelli"
        print(f"{animale} appartiene alla categoria dei {animal_type}!")
    
    case animale if animale in ["squalo", "trota", "salmone", "carpa"]:
        animal_type = "Pesci"
        print(f"{animale} appartiene alla categoria dei {animal_type}!")
    
    case _:
        print(f"{animale} non appartiene a nessuna categoria riconosciuta.")

animale_info = {"nome": animale, "categoria": animal_type, "habitat": habitat}

match (animal_type, habitat):
    
    case ("Mammiferi", "acqua") if animale in ["balena", "delfino"]:
        print(f"L'animale {animale} è uno dei mammiferi che può vivere nell'acqua!")
    
    case ("Mammiferi", "terra"):
        print(f"L'animale {animale} è uno dei mammiferi che può vivere sulla terra!")
    
    case ("Rettili", "terra"):
        print(f"L'animale {animale} è uno dei rettili che può vivere sulla terra!")
    
    case ("Uccelli", "aria"):
        print(f"L'animale {animale} è uno degli uccelli che può vivere nell'aria!")
    
    case ("Pesci", "acqua"):
        print(f"L'animale {animale} è uno dei pesci che può vivere nell'acqua!")
    
    case _:
        print(f"Attenzione: l'animale {animale} non può vivere nell'habitat {habitat}." if animal_type != "unknown" else f"Errore: l'animale {animale} o l'habitat {habitat} non sono riconosciuti.")