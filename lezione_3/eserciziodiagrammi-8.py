#eserciziodiagrammi-8

a = int(input("Inserire un numero: "))
b = int(input("Inserire un numero: "))

if a >= b:

    print("A deve essere minore di B")

elif a <= 0 and b <= 0:

    print("A e B devono essere positivi")

elif a%1!=0 and b%1!=0:
    
    print("A e B devono essere interi")

sum = 0
i = a

while True:
    if i > b:
        print(sum)
        break

    else:
        i += 1
        sum += 1