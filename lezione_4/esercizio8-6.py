#esercizio8-6

def city_country(city : str = "Santiago", country : str = "Chile"):

    return f"{city},{country}"

city1 = city_country("Santiago", "Chile")
city2 = city_country("Paris", "France")
city3 = city_country("Tokyo", "Japan")

print(city1)
print(city2)
print(city3)