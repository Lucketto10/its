# scrivere il frammento di codice che cambi il valore intero memorizzato nella variabile x nel seguente modo:
# - se x è pari, deve essere diviso per 2;
# - se x è dispari deve essere moltiplicato per 3 e gli deve essere sottratto 1.

n : input = 42.0

def collatz(n : float) -> float:

    if n % 2 == 0:

        return n / 2

    else:

        return(3 * n) + 1

risultato : float = collatz(n=n)
print(risultato)
----------------------------------------------------------------------
