class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(bob.name)

if bob.age > alice.age:
    
    print(bob.age)

else:
    print(alice.age)


luca = Person("Luca T.", 19)
alessio = Person("Alessio R.", 20)
diego = Person("Diego L.", 26)
people = (diego, luca, alessio, bob, alice)


min_age = people[0]
for i in people:
    if i.age < min_age.age:
        min_age = i

print(f"Il più giovane è: {min_age.name} {min_age.age}") 