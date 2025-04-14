def produttoria_pi3(n):
    if n == 1:
        return 1
    else:
        return (n ** 3) * produttoria_pi3(n - 1)

n = 5
risultato = produttoria_pi3(n)
print(f"Il valore della produttoria Pi3 per n={n} è: {risultato}")
