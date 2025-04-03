#esercizifunzioniricorsive5

def sumInRange(a:int, b:int) -> int:

    if a > b:

        temp:int = a

        a = b
        b = temp 

    sum:int = 0

    while b >= a:
        sum += b
        b -= 1

    return int(sum)

print(sumInRange(5, 10))
