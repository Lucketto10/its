
#esercizio3C7
testa = 0
croce = 0
i = 1

for i in range(8):
    moneta : str = str(input("Lancia moneta: "))

    match moneta:
        case moneta if moneta == "t" or  moneta == "T":
            testa += 1
            i += 1 

        case moneta if moneta == "c" or moneta == "C":
            croce += 1
            i += 1

        case _:
            print("Una moneta può avere solo o testa o croce")


percentuale_testa : float = (testa / i) * 100
percentuale_testa : float = (round(percentuale_testa, 2))
print(f"La percentuale dei risultati testa totali è: {percentuale_testa}%")

percentuale_croce : float = (croce / i) * 100
percentuale_croce : float = (round(percentuale_croce, 2))
print(f"La percentuale dei risultati croce è: {percentuale_croce}%")
