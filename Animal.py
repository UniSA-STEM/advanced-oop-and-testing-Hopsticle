'''
File: Staff.py
Description: This module contains the different animals as well as their characteristics
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''


class Animal:
    def __init__(self, name, species=None, age=0, diet=None, size=None):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.size = size


class Reptile(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound='hiss'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''snake, lizard, crocodile, turtle'''

class Crocodile(Reptile):
    def __init__(self, name, species=None, age=0, diet=None, sound='hiss'):
        Reptile.__init__(self, name, species, age, diet, sound)

class Snake(Reptile):
    def __init__(self, name, species=None, age=0, diet=None, sound='hiss'):
        Reptile.__init__(self, name, species, age, diet, sound)

class Lizard(Reptile):
    def __init__(self, name, species=None, age=0, diet=None, sound='hiss'):
        Reptile.__init__(self, name, species, age, diet, sound)

class Turtle(Reptile):
    def __init__(self, name, species=None, age=0, diet=None, sound='hiss'):
        Reptile.__init__(self, name, species, age, diet, sound)

class Feline(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound='roar'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''lion, tiger, panther'''

class Lion(Feline):
    def __init__(self, name, species=None, age=0, diet=None, sound='roar'):
        Feline.__init__(self, name, species, age, diet, sound)

class Tiger(Feline):
    def __init__(self, name, species=None, age=0, diet=None, sound='roar'):
        Feline.__init__(self, name, species, age, diet, sound)

class Panther(Feline):
    def __init__(self, name, species=None, age=0, diet=None, sound='roar'):
        Feline.__init__(self, name, species, age, diet, sound)



class Canine(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound='woof'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''dingo, wolf, fenneck fox'''

class Dingo(Canine):
    def __init__(self, name, species=None, age=0, diet=None, sound='woof'):
        Canine.__init__(self, name, species, age, diet, sound)

class Wolf(Canine):
    def __init__(self, name, species=None, age=0, diet=None, sound='woof'):
        Canine.__init__(self, name, species, age, diet, sound)

class Fenneck(Canine):
    def __init__(self, name, species=None, age=0, diet=None, sound='woof'):
        Canine.__init__(self, name, species, age, diet, sound)



class Marsupial(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound='tck tck'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''kangaroo, bilby, tasmanian devil'''

class Kangaroo(Marsupial):
    def __init__(self, name, species=None, age=0, diet=None, sound='tck tck'):
        Marsupial.__init__(self, name, species, age, diet, sound)

class Billy(Marsupial):
    def __init__(self, name, species=None, age=0, diet=None, sound='tck tck'):
        Marsupial.__init__(self, name, species, age, diet, sound)

class TasmanianDevil(Marsupial):
    def __init__(self, name, species=None, age=0, diet=None, sound='tck tck'):
        Marsupial.__init__(self, name, species, age, diet, sound)



class Ailuridae(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound='kck'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''red panda'''

class RedPanda(Ailuridae):
    def __init__(self, name, species=None, age=0, diet=None, sound='kck'):
        Ailuridae.__init__(self, name, species, age, diet, sound)


class Fish(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound ='blub'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''barracuda, clown fish, piranha, puffer fish'''

class Barracuda(Fish):
    def __init__(self, name, species=None, age=0, diet=None, sound='blub'):
        Fish.__init__(self, name, species, age, diet, sound)

class ClownFish(Fish):
    def __init__(self, name, species=None, age=0, diet=None, sound='blub'):
        Fish.__init__(self, name, species, age, diet, sound)

class Piranha(Fish):
    def __init__(self, name, species=None, age=0, diet=None, sound='blub'):
        Fish.__init__(self, name, species, age, diet, sound)

class PufferFish(Fish):
    def __init__(self, name, species=None, age=0, diet=None, sound='blub'):
        Fish.__init__(self, name, species, age, diet, sound)


class Bird(Animal):
    def __init__(self, name, species=None, age=0, diet=None, sound = 'caw'):
        Animal.__init__(self, name, species, age, diet, sound)
        '''penguin, pheasant, peacock'''

class Penguin(Bird):
    def __init__(self, name, species=None, age=0, diet=None, sound = 'caw'):
        Bird.__init__(self, name, species, age, diet, sound)

class Pheasant(Bird):
    def __init__(self, name, species=None, age=0, diet=None, sound = 'caw'):
        Bird.__init__(self, name, species, age, diet, sound)

class Peacock(Bird):
    def __init__(self, name, species=None, age=0, diet=None, sound = 'caw'):
        Bird.__init__(self, name, species, age, diet, sound)
