#eserciziodiagrammi-3

nome_corso = input(f"Inserisci il nome del corso")
max_posti = 100

while True :
    opzione = input(f"inserisci opzione")

    if opzione == "iscrivi" :

        if max_posti > 0 :

            max_posti = max_posti - 1

        else :

            print(f"non ci sono posti disponibili")

    if opzione == "annulla" :

        if max_posti < 100 :

            max_posti = max_posti + 1

        else :
            print(f"tutti i posti posti sono gia disponibili")
    
    if opzione == "visualizza" :

        print(f"i posti massimi sono {max_posti}")
        print(f"i posti liberi sono {100 - max_posti}")

    if opzione == "elimina" :

        nome_corso = input(f"inserisci nome del corso")

    if opzione == "esci" :

        break