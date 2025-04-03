#eserciziodiagrammi-2

nord_sud = int(input(f"Inserisci veicoli direzione nord_sud "))
est_ovest = int(input(f"Inserisci veicoli direzione est_ovest "))
soglia = 70

if nord_sud > soglia and est_ovest > soglia :

    time_ns = 50
    time_eo = 50

elif nord_sud > soglia :

    time_ns = 60
    time_eo = 40

elif est_ovest > soglia :

    time_ns = 40 
    time_eo = 60

else :
    
    time_ns = (nord_sud/(nord_sud + est_ovest)) * 100
    time_eo = (nord_sud/(nord_sud + est_ovest)) * 100

print(f"Il testo assegnato alla direzione nord_sud è {time_ns}")
print(f"Il testo assegnato alla direzione est_ovest è {time_eo}")

