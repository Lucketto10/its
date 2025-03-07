#eserciziodiagrammi10

r = int(input("Inserire il proprio reddito: "))
m = int(input("Inserire la propria media: "))

if r < 20000 and m > 27:
    print("Borsa di studio approvata")

else:
    print("Borsa di studio rifiutata per reddito troppo alto o media troppo bassa")