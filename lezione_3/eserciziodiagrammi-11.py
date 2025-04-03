#eserciziodiagrammi-11

while True:
    n = float(input("Inserisci n: "))
    if n%1==0:
        if n%2==2 and n > 10:
            print("Numnero valido")
        else:
            print("Numero non valido")
            