#esercizio2_Match_Statement

nome = input("Inserisci il tuo nome: ")
gender = input("Inserisci il tuo genere (m/f): ")

match gender:
    case "m":

        print(f"Nome {nome}\nGenere: Maschio")
    
    case "f":
        print(f"Nome {nome}\nGenere: Femmina ")

    case _:
        print("errore: genere non valido non è possibile generare un documento di identità.")
