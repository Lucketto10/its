#eserciziodiagramma-14
punteggio= 0
while punteggio <100:
    D1 = int(input(f"inserisci valore D1: "))
    D2 = int(input(f"inserisci valore D2: "))
    if D1 > 0 and D1 <= 6 and D2 > 0 and D2<=6:
        somma = D1 + D2
        if D1 % 2 == 0 and D2 % 2 == 0 and somma > 8:
            punteggio = 100
            print(punteggio)
        elif D1 == 6 or D2 == 6 or somma == 7:
            punteggio+= 10
            print(punteggio)
        else:
            punteggio= 0
            print("sconfitta")
print("vittoria")
#ciao

