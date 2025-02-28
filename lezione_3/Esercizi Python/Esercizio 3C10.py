'''Esercizio 3C-10. Scrivere un programma in Python che permetta all'utente di inserire una data (giorno e mese espressi in forma numerica),
 salvi la data in una tupla e utilizzi un match statement per verificare se la data corrisponde a una festività o a un evento speciale:

 Capodanno → 1 Gennaio → "Capodanno"
 San Valentino → 14 Febbraio → "San Valentino"
 Festa della Repubblica Italiana → " Giugno → "Festa della Repubblica Italiana"
 Ferragosto → 15 Agosto → "Ferragosto"
 Halloween → 31 Ottobre → "Halloween"
 Natale → 25 Dicembre → "Natale"
 Altro caso → "Nessuna festività importante in questa data."
 '''

#esercizio3C10

giorno = int(input("Inserisci il giorno: "))
mese = str(input("Inserisci mese: "))

data = (giorno, mese)

match data: 
    case data if giorno == 1 and mese == "Gennaio":
        print("Capodanno")
    
    case data if giorno == 14 and mese == "Febbraio":
        print("San Valentino")
    
    case data if giorno == 2 and mese == "Giugno":
        print("Festa della Repubblica Italiana")
    
    case data if giorno == 15 and mese == "Agosto":
        print("Ferragosto")
    
    case data if giorno == 31 and mese == "Ottobre":
        print("Halloween")
    
    case data if giorno == 25 and mese == "Dicembre":
        print("Natale")

    case _:
        print("Nessuna festività importante in questa data.")