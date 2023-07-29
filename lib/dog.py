#!/usr/bin/env python3


class Dog:
    def __init__(self, name, breed="Mutt", favorite_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy
        self.breed = breed
        # print(f"{name} is born!")

    def bark(self):
        print("Woof!")

    def showing_self(self):
        return self

    def get_adopted(self, owner_name):
        self.owner = owner_name


fido = Dog("Fido")
fido.breed = "Dalmation"
fido.favorite_toy
# Any
#fido.owner = "Sophie"
fido.name
fido.get_adopted("Sophie")
fido.owner
# fido.showing_self()
# adopt(fido, "Sophie")


snoopy = Dog("Snoopy", "Tennis Ball")
snoopy.favorite_toy
# Tennis Ball
snoopy.breed = "Beagle"
snoopy.name
