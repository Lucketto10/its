#eserciziodiagramma1-2

massimo : int = int(input("Inserisci valore massimo: "))

count = 1

while True:
     
     n : int = int(input("Inserisci altri valori: "))

     if n > massimo:
          
          massimo = n 

          count += 1
        
          if count == 4:
               break
          
          print(f"Il massimo valore è {massimo}")