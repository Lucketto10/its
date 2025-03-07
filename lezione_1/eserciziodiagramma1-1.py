#eserciziodiagramma1.1

massimo : int = int(input("Inserisci primo valore: "))

count = 1

while count < 4:
   
    count += 1 

    n : int = int(input("Inserisci altri valori: "))

    if n > massimo:

        massimo = n

    else:
        continue

print(f"Il numero più grande è {massimo}")