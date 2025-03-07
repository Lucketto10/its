#eserciziodiagramma5

n : float = float(input("Inserisci un numero: "))

if n < 2:

    print(f"Il numero {n} non è primo")

else:

    div = 2
    is_prime = True

    while div < n:

        if n % div == 0:

            is_prime = False
            break 
        div += 1

    if is_prime:
        print(f"Il numero {n} è primo")
    else:
        print(f"Il numero {n} non è primo")
