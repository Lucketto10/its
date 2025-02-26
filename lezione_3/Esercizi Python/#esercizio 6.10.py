#esercizio 6.10
numeri = {"Luca": [16, 19, 30],
        "Claudia":[23, 53, 73],
         "Diego": [21, 14, 65],  
         "Mario" : [17, 24, 18],  
         "Mattia" : [62, 35, 26]} 


for person, numbers in numeri.items():
    print(f"{person}]")
    for number in numbers:
       print(f"{number}")
