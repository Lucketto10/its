#eserciziodiagramma9

nome = str(input("Inserire il nome: "))
vendite = int(input("Inserire le vendite: "))
max_nome = nome 
min_nome = nome 
max = vendite 
min = vendite

for i in range(19):
    new_nome = str(input("Insrire un nuovo nome: "))
    new_vendite = int(input("Insrire vendite nuove: "))

    if new_vendite > max:

        max_nome = new_nome

        max = new_vendite
    
    elif new_vendite < min:

        new_nome = new_nome

        min = new_vendite
    
print(f"La persona con più vendite è {max_nome} con {max} vendite")
print(f"La persona con meno vendite è {min_nome} con {min} vendite")
