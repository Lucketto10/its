#eserciziodiagrammi-19

while True:

    n = int(input("Inserire un numero: "))

    if n %1==0:
        break

    else:
        continue

if n<0:

    print("Inserire un numero maggiore di 0")

else:

    if n%2==0:
        cont = 4
        result = 0
    
        while cont <=n:

            result += cont
            cont += 4

        print(result)
    
    else:
        cont = 1
        result = 1

        while cont <= n:
            result*= cont
            cont +=2
        
        print(result)