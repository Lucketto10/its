#esercizio 6.9
favorite_places = {'Luca': ['Paris', 'Tokyo', 'New York'],
                   'Claudia':['Mout Everest', 'Gran Canyon', 'London'],
                   'Diego': ['Rome', 'Berlin', 'Sydney', 'Barcelona']}

for name, places in favorite_places.items():
    print(f"{name}]")
    for place in places:
       print(f"{place}")
