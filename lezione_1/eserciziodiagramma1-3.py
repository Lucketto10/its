#eserciziodiagramma1-3

massimo : int = int(input("Inserisci valore massimo:"))


for i in range(3):
        
         n: int = int(input("Inserisci altri numeri: "))

         if n > massimo:
                massimo = n 

                print(f"il numero massimo è {massimo}")
        
