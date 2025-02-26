#esercizio1_Match_Statement

n : int = int (input ("inserisci i numeri di neonati"))

match n:
    
    case 1:

        print(f"Congratulazioni")
    
    case 2:

        print(f"Wow! Gemelli!")

    case 3:

        print(f"Wow! Tre!")

    case 4:

        print(f"Mamma mia Quattro! Wow!")

    case 5:

        print(f"Incredibile! Cinque!")

    case _:
        
        print(f"Non ci credo! {n}  bambini!")