#eserciziodiagrammi5

n = int(input("Inserisci un numero intero positivo intero: "))

if n <= 0:
    print("Errore, n deve essere positivo")

else:
    sum = 0
    i = 1 

    while i <= n :
        sum += i
        i += 1

    print("La somma è:", sum)