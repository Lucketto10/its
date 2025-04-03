#esercizio8-16

import nomi
print(nomi.greet("Alice"))

from nomi import greet
print(greet("Mario"))

from nomi import greet as fn
print(fn("Luca"))

import nomi as mn 
print(mn.greet("Claudio"))

from nomi import *
print(greet("Diego"))