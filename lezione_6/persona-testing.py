#persona-testing.py
from persona1 import Persona

lt : Persona = Persona("Luca", "Taggiasco", 19)

print(lt)

print(lt.name, lt.lastname, lt.age)
#sfrutto la funzione della displayData della classe Persona per visualizzare in input i dati relativi alla persona lt

lt.displayData() 
