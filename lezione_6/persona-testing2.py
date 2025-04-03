#persona-testing2.py

from persona2 import Persona

lt:Persona = Persona()

lt.displayData()

print("---------------")

#imposto il nome della persona lt
lt.setName("Luca")
lt.displayData()

#imposto il cognome della persona lt
lt.setLastname("Taggiasco")


#imposto l'età della persona lt
lt.setAge(19)

print("---------------")

lt.displayData()

print("---------------")

print(lt.getName(), lt.getLastname(), lt.getAge())