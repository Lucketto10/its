#esercizi_lezione2
# esercizio 2.3
person_name = "Eric"

print(f"Hello {person_name}, would you like to learn some Python today?")
#esercizio 2.4
person_name = "Eric"

print(person_name.lower())   
print(person_name.upper())    
print(person_name.title())   

#esercizio 2.5
quote = "A person who never made a mistake never tried anything new."
author = "Albert Einstein"

print(f'{author} once said, “{quote}”')

#esercizio 2.6
famous_person = "Albert Einstein"

quote = "A person who never made a mistake never tried anything new."

message = f'{famous_person} once said, “{quote}”'

print(message) 

#esercizio 3.1
names = ["Alice", "Bob", "Charlie", "Diana"]

for name in names:
    print(name)
#esercizio 3.2
names = ["Alice", "Bob", "Charlie", "Diana"]

for name in names:
    print(f"Hello {name}, I hope you’re having a great day!")

#esercizio 3.3 
transportation_modes = ["Honda motorcycle", "Tesla car", "Boeing airplane", "Harley Davidson bike"]

for mode in transportation_modes:
    print(f"I would like to own a {mode}.")

#esercizio 3.4
guests = ["Albert Einstein", "Marie Curie", "Mahatma Gandhi"]

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!") 

#esercizio 3.5
guests = ["Albert Einstein", "Marie Curie", "Mahatma Gandhi"]

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")

print("\nUnfortunately, Mahatma Gandhi can't make it to dinner.")

guests[2] = "Nikola Tesla"

print("\nHere are the updated invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!") 

#esercizio 3.6
guests = ["Albert Einstein", "Marie Curie", "Mahatma Gandhi"]

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")

print("\nUnfortunately, Mahatma Gandhi can't make it to dinner.")

guests[2] = "Nikola Tesla"

print("\nI just found a bigger table, so there's more room for more guests!")

guests.insert(0, "Isaac Newton")  
guests.insert(2, "Leonardo da Vinci")  
guests.append("Winston Churchill")  

print("\nHere are the updated invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")

#esercizio 3.7 
guests = ["Isaac Newton", "Albert Einstein", "Leonardo da Vinci", "Marie Curie", "Nikola Tesla", "Winston Churchill"]

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner!")

print("\nI just found out that my new dinner table won't arrive in time, so I can only invite two people.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\nThe following guests are still invited:")
for guest in guests:
    print(f"Dear {guest}, you’re still invited to dinner!")

del guests[:]

print("\nHere is the final guest list:", guests)
 
 #esercizio 3.8
places = ["Paris", "Tokyo", "Cairo", "New York", "Sydney"]

print("Original list:")
print(places)

print("\nAlphabetical order:")
print(sorted(places))

print("\nOriginal list after sorted() is applied:")
print(places)

print("\nReverse-alphabetical order:")
print(sorted(places, reverse=True))

print("\nOriginal list after reverse sorted() is applied:")
print(places)

places.reverse()
print("\nList after reverse() is applied:")
print(places)

places.reverse()
print("\nList after reverse() is applied again (back to original order):")
print(places)

places.sort()
print("\nList after sort() is applied (alphabetical order):")
print(places)

places.sort(reverse=True)
print("\nList after sort() is applied (reverse-alphabetical order):")
print(places) 

#esercizio 3.9
guests = ["Isaac Newton", "Albert Einstein", "Leonardo da Vinci", "Marie Curie", "Nikola Tesla", "Winston Churchill"]

print(f"\nI am inviting {len(guests)} people to dinner.") 

#esercizio 3.10
countries = ["Canada", "Japan", "Australia", "Brazil", "Germany"]

print("Original list of countries:")
print(countries)

print("\nCountries in alphabetical order (using sorted()):")
print(sorted(countries))

print("\nOriginal list after sorted() is applied:")
print(countries)

print("\nCountries in reverse-alphabetical order (using sorted()):")
print(sorted(countries, reverse=True))

print("\nOriginal list after reverse sorted() is applied:")
print(countries)

countries.reverse()
print("\nList after reverse() is applied:")
print(countries)

countries.reverse()
print("\nList after reverse() is applied again (back to original order):")
print(countries)

countries.sort()
print("\nList after sort() is applied (alphabetical order):")
print(countries)

countries.sort(reverse=True)
print("\nList after sort() is applied (reverse-alphabetical order):")
print(countries)
print("\nThe number of countries in the list is:", len(countries))

countries.append("India")
print("\nList after append() is applied (added India):")
print(countries)

countries.insert(0, "United States")
print("\nList after insert() is applied (added United States at the beginning):")
print(countries)

removed_country = countries.pop()
print(f"\nThe country '{removed_country}' was removed from the list using pop().")
print("List after pop() is applied:")
print(countries)

del countries[2]
print("\nList after del is applied (removed country at index 2):")
print(countries)

countries.clear()
print("\nList after clear() is applied (all countries removed):")
print(countries)
 