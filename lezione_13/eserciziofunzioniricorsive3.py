#eserciziofunzioniricorsive3

def sum(n:int) -> int:

    if n < 0:
        print("Error! Inserted number is negative!")
        return None

    else:

        sum:int = 0

        while n:
            sum += n
            n -= 1
        print(sum)
        return int(sum)
sum(5)
sum(-5)