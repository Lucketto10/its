#esercizio 6.8
cane: dict={"animale":"cane", "razza":"bulldog", "padrone": "laghetti"} 
uccello: dict={"animale":"uccello", "razza":"pappagallo", "padrone": "caico"} 
gatto: dict={"animale":"gatto", "razza":"sfinks", "padrone": "farallo"} 

pets = [cane, uccello, gatto]  

for i in pets:
    print(f"animale: {i['animale']}")
    print(f"razza: {i['razza']}")
    print(f"padrone: {i['padrone']}")
