#eserciziodiagramma3

somma = 0
count = 0

while True:

    n : float = float(input("Inserisci un numero: "))

    if n > 0:

        somma += n

    else: 
        continue
    count += 1

    if count > 5:
        break
print(f"La somma totale è {somma}")