#esercizio3C2
voto : int = int(input("Converti voto laurea"))

match voto:
    case voto if voto >= 106 and  voto <= 110:
        print("Il voto è 4")

    case voto if voto >= 101 and voto <= 105:
        print("Il voto è 3.7")

    case voto if voto >= 96 and voto <= 100:
        print("Il voto è 3.3")
    
    case voto if voto >= 91 and voto <= 95:
        print("Il voto è 3")

    case voto if voto >= 86 and voto <= 90:
        print("Il voto è 2.7")
    
    case voto if voto >= 81 and voto <= 85:
        print("Il voto è 2.3")

    case voto if voto >= 76 and voto <= 80:
        print("Il voto è 2")

    case voto if voto >= 70 and voto <= 75:
        print("Il voto è 1.7")

    case voto if voto >= 66 and voto <= 69:
        print("Il voto è 1")

    case _: 
        print("Voto non valido")


