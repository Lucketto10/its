#eserciziodiagramma-16
n = int(input("Inserisci n: "))
if n%1==0:
    if n > 0 and n <= 100:
        somma = 0
        i = 1
        while i < n:
            if i%2==0:
                somma+=i
            i+=1
        print(somma)
    elif n == 0 or n < 0:
        print("errore")
    else:
        somma = 0
        i = 1
        while i < n:
            if i % 2 != 0:
                somma += i
            i+= 1
        print(somma)