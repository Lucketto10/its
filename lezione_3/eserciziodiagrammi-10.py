#eserciziodiagrammi-10

età = int(input("Inserisci eta: "))
if età >= 10 and età <= 65:
    print("Puoi partecipare all'attività")
elif età > 18:
    print("Non puoi partecipare all'attività perchè non hai raggiunto l'età richiesta")
else:
    print("Non puoi partecipare all'attività perchè hai superato l'età massima complessiva")
