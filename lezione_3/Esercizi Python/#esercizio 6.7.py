#esercizio 6.7
persona1: dict={"nome":"diego", "cognome":"laghetti", "età": 19, "città":"Roma"} 
persona2: dict={"nome":"mario", "cognome":"rossigni", "età": 18, "città":"Roma"} 
persona3: dict={"nome":"edoardo", "cognome":"carfora", "età": 20, "città":"Roma"}

people = [persona1, persona2, persona3]  

for i in people:
    print(f"nome: {i['nome']}")
    print(f"cognomne: {i['cognome']}")
    print(f"età: {i['età']}")
    print(f"città: {i['città']}")
