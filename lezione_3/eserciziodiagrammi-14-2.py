#eserciziodiagrammi-15

punteggio = 0 
while True:     
    d1 = int(input(f"inserisci valore d1: "))
    d2 = int(input(f"inserisci valore d2: "))
    if d1 > 0 and d1 <= 6 and d2 > 0 and d2 <= 6:
        somma = d1 + d2
        if d1 % 2 == 0 and d2 % 2 == 0 and somma > 8:
            punteggio  = 100
            print(punteggio)
        elif d1 == 6 or d2 == 6 or somma == 7:
            punteggio += 10
            print(punteggio)
            continue
        else:
            punteggio = 0 
    if punteggio >= 100 or punteggio == 0:
        if punteggio >= 100:
            print("vittoria")
            break
        else: 
            print("sconfitta")
            break