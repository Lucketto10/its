#esercizidiagramma6

while True:
    n = int(input("Inserire un numero: "))
    
    if n > 0:
        break
    else: 
        print("Inserire un numero positivo")
     
fattoriale = 1
i = 1

for i in range (1, n+1):

    fattoriale *= i

print (f"Il fattoriale di {n} è {fattoriale}  ")