#eserciziodiagrammi-18
while True:

    n = int(input("Quanti numeri sono da inserire?: "))

    if n %1==0:
        break

    else:
        continue

i = 1
somma=0
madia=0
somma_pari=0
somma_dispari=0

while i-1 != n:

    while True:

        x = int(input("Inserire un nuovo numero: "))

        if x%1==0:
            break
        else:
            continue

    somma += x    
    media = somma/i

    if x%2==0 and x>media:

        somma_pari +=x

    
    if x<media or x%2!=0:

        somma_dispari +=x

    i +=1

print(f"La somma dispari è {somma_dispari}")
print(f"La somma pari è {somma_pari}")

if somma_pari > somma_dispari:

    print("La somma pari è maggiore")

elif somma_pari < somma_dispari:

    print("La somma dispari è maggiore")

else:

    print("Le somme sono uguali")