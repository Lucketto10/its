#eserciziodiagrammi-7

cont = 0
sum = 0

while True:
    scelta = str(input("Inserire scelta. "))

    if scelta == "si":
        while True:
            voto = int(input("Inserire il voto: "))

            if voto > 0 :
                cont += 1
                sum += voto
                break
            else:
                print("Errore")
                continue

    elif scelta == "no":

        if cont > 0:

            media = sum/cont

            print(f"La media è {media}")
            break
        else:
            print("Nessun voto inserito")
            break
    else:
        continue