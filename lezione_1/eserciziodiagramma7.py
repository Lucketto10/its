#eserciziodiagramma7

pari = 0 
dispari = 0
cont = 0 

while True:
    if cont == 10:
        print("I numeri pari sono: ",pari)
        print("I numeri dispari sono: ",dispari)

        break

    else:
        n = int(input("Inserisci numero: "))
        if n % 2 == 0:
            pari += 1

        else:
            dispari += 1

    cont += 1