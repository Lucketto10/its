#eserciziodiagrammi-17

#flowchart17
temp_max = -100000
day_max = 0 
temp_min = 100000
day_min = 0 
cont_norma = 0 
t_media = 0 
i = 1 
while i <= 7 : 
    temp = int(input("Inserisci temperatura: "))
    t_media += temp 
    if temp > temp_max : 
        temp_max = temp 
        day_max = i  
    elif temp < temp_min : 
        temp_min = temp 
        day_min = i 
    if temp >= 10 and temp <= 30 : 
        cont_norma += 1 
        if cont_norma == 7 : 
            print(f"temperature nella norma")
        else : 
            i += 1
    elif temp < 5 or temp > 35 : 
        print(f"allerta temperatura ")

t_media = t_media/7
print(f"la temperatura media è {t_media}")
print(f"la temperatura massima è {temp_max}")
print(f"la temperatura minima è {temp_min}")
print(f"la temperatura massima del giorno è {day_max}")
print(f"la temperatura minima del giorno è {day_min}")