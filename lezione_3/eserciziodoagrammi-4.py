#eserciziodoagrammi-4

tutor = 10
attesa = 0

while True :
    studente = str(input("Inserire lo studente: "))

    if tutor > 0 :
        tutor += 1
        print("Tutor assegnato con successo")

    else :
        attesa += 1
        print("Studente in attesa")

    if tutor == 0 and attesa == 40:
        break 

    else :
        continue