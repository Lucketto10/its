from persona import Persona 
from studente import studente

p = Persona('alessio',"riboldi",29)
print(p)

studente1 = studente('alessio','giggetto',29,'39493932')
print(studente1)

if isinstance(studente1, studente):

    print(f"\n studente 1 è istanza della classe Studente")

if isinstance(studente1,Persona) : 

    print("\n studente1 è un oggetto della classe studente ma anche un oggetto della classe persona")