#eserciziodiagramma8

soglia = int(input("Inserisci una soglia: "))

cont = 0

for i in range (7):

    n = int(input("Inserire un numero: "))

    if n > soglia:
        print(f"{n} E' sopra la soglia")

cont += 1