#eserciziodiagramma-17

dispari = 0
pari = 0
negativi = 0
positivi = 0
i = 0 
while i != 10:
    n = int(input("Inserisci n: "))
    if n%1==0 and n != 0:
        if n > 0:
            positivi += 1
            if n%2==0 and n > 20:
                pari += 1
        else: 
            negativi += 1
            if n%2!=0 or n < -10:
                dispari += 1
    i += 1
print("I positivi sono",positivi)
print("I negativi sono",negativi)
print("I pari sono",pari)
print("I dispari sono",dispari)