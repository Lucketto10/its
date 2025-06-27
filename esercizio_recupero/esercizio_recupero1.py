while True:
    try:
        x = int(input("Inserisci il numero x (intero positivo): "))
        if x > 0:
            break
        else:
            print("Devi inserire un intero positivo.")
    except:
        print("Input non valido. Riprova.")

sequenza = []
print("Inserisci una sequenza di interi positivi (0 per terminare):")
while True:
    try:
        numero = int(input("Numero: "))
        if numero == 0:
            break
        elif numero > 0:
            sequenza.append(numero)
        else:
            print("Devi inserire un intero positivo.")
    except:
        print("Input non valido. Riprova.")

print("\nLa sequenza inserita è:", sequenza)

occorrenze = 0
for n in sequenza:
    if n == x:
        occorrenze += 1

posizione = -1
for i in range(len(sequenza)):
    if sequenza[i] == x:
        posizione = i + 1
        break
somma_diversi = 0
for n in sequenza:
    if n != x:
        somma_diversi += n

if occorrenze == 1:
    print(f"Il numero {x} compare 1 sola volta nella sequenza.")
else:
    print(f"Il numero {x} compare {occorrenze} volte nella sequenza.")

if posizione != -1:
    print(f"Il numero {x} compare per la prima volta in posizione {posizione} nella sequenza.")
else:
    print(f"Il numero {x} non compare nella sequenza.")

print(f"La somma dei valori della sequenza diversi da {x} è {somma_diversi}.")
