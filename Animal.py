'''
File: Animals.py
Description: This module contains the different animals as well as their characteristics
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

all_animals = []


class Animal(ABC):
    def __init__(self, name, species=None, age=0, diet=None, size=None, is_cold_blooded=False, sound=None, biome=None,
                 health=None):
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.size = size
        self.is_cold_blooded = is_cold_blooded
        self.sound = sound
        self.biome = biome
        self.health = health

    @abstractmethod
    def speak(self):
        pass

    def get_description(self):
        return f'{self.name} is a {self.age} year old {self.species}'

    #TODO Format health Records
    def HealthRecord(self):
        return print(
               f'________________________________________'
            f'\n|  Name: {self.name}    Age: {self.age}  |'
            f'\n|  Species: {self.species}               |'
            f'\n|  Diet: {self.diet}                     |'
            f'\n|  Health Condition: {self.health}       |'
            f'\n|                                        |'
            f'\n|                                        |'
            f'\n|________________________________________')

    #TODO Add animals with random names
    def AddAnimal(self, name, species=None, age=0, diet=None):
        new_animal = Animal(name, species, age, diet, species)
        all_animals.append(new_animal)
        return new_animal
        print(f'New animal: {new_animal} added ')
    #TODO when adding new animal ensure there is an enclosure ready to move into with enough space

class Reptile(Animal):
    def __init__(self, name, species=None, age=0, diet='Meat', size=None, is_cold_blooded=True, sound=None, biome=None):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return 'Hiss'


class Crocodile(Reptile):
    def __init__(self, name, size=3, biome='Swamp'):
        super().__init__(name, 'Crocodile', size=size, biome=biome)

    def speak(self):
        return 'Beeeeellollolloloow'


class Snake(Reptile):
    def __init__(self, name, size=1.5, biome='Forest'):
        super().__init__(name, 'Snake', size=size, biome=biome)

    def speak(self):
        return super().speak() + 'sssss'


class Iguana(Reptile):
    def __init__(self, name, size=1, biome='Brush'):
        super().__init__(name, 'Iguana', size=size, biome=biome)

    def speak(self):
        return super().speak()


class Turtle(Reptile):
    def __init__(self, name, diet='Plants', size=1, biome='Water'):
        super().__init__(name, 'Turtle', diet=diet, size=size, biome=biome)

    def speak(self):
        return super().speak()


class Feline(Animal):
    def __init__(self, name, species=None, age=0, diet='Meat', size=2, is_cold_blooded=False, sound=None,
                 biome='Jungle'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return 'ROOOARRR'


class Lion(Feline):
    def __init__(self, name, biome='Savannah'):
        super().__init__(name, 'Lion', biome=biome)

    def speak(self):
        return super().speak()


class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name, 'Tiger')

    def speak(self):
        return super().speak()


class Panther(Feline):
    def __init__(self, name):
        super().__init__(name, 'Panther')

    def speak(self):
        return super().speak()


class Canine(Animal):
    def __init__(self, name, species=None, age=0, diet='Meat', size=None, is_cold_blooded=False, sound=None,
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound


class Dingo(Canine):
    def __init__(self, name, size=1):
        super().__init__(name, 'Dingo', size=size)

    def speak(self):
        return 'Wooof'


class Wolf(Canine):
    def __init__(self, name, size=1.5, biome='Forest'):
        super().__init__(name, 'Wolf', size=size, biome=biome)

    def speak(self):
        return 'Hoooowwlllll'


class FennecFox(Canine):
    def __init__(self, name, size=.5):
        super().__init__(name, 'Fennec Fox', size=size)

    def speak(self):
        return 'Yip'


class Marsupial(Animal):
    def __init__(self, name, species=None, age=0, diet='Plants', size=None, is_cold_blooded=False, sound=None,
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound


class Kangaroo(Marsupial):
    def __init__(self, name, size=1.5):
        super().__init__(name, 'Kangaroo', size=size)

    def speak(self):
        return 'Booiiiing'


class Billy(Marsupial):
    def __init__(self, name, size=.5):
        super().__init__(name, 'Bilby', size=size)

    def speak(self):
        return 'Tck tck'


class TasmanianDevil(Marsupial):
    def __init__(self, name, size=.5):
        super().__init__(name, 'Tasmanian Devil', diet='Meat', size=size)

    def speak(self):
        return 'SCCREEEEEEEEE'


class Ailuridae(Animal):
    def __init__(self, name, species=None, age=0, diet='Meat/Plants', size=.5, is_cold_blooded=False, sound=None,
                 biome='Jungle'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound


class RedPanda(Ailuridae):
    def __init__(self, name):
        super().__init__(name, 'Red Panda')

    def speak(self):
        return super().speak()


class Fish(Animal):
    def __init__(self, name, species=None, age=0, diet='Plants', size=None, is_cold_blooded=True, sound='Glub Glub',
                 biome='Water'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound


class Barracuda(Fish):
    def __init__(self, name, diet='Meat', size=1):
        super().__init__(name, 'Barracuda', diet=diet, size=size)

    def speak(self):
        return super().speak()


class ClownFish(Fish):
    def __init__(self, name, size=.2):
        super().__init__(name, 'Clown Fish', size=size)

    def speak(self):
        return super().speak()


class Piranha(Fish):
    def __init__(self, name, diet='Meat', size=.2):
        super().__init__(name, 'Piranha', diet=diet, size=size)

    def speak(self):
        return super().speak()


class PufferFish(Fish):
    def __init__(self, name, size=.2):
        super().__init__(name, 'Puffer Fish', size=size)

    def speak(self):
        return super().speak()


class Bird(Animal):
    def __init__(self, name, species=None, age=0, diet='Plants', size=.5, is_cold_blooded=False, sound='CAAAW',
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound


class Penguin(Bird):
    def __init__(self, name, diet='Meat', biome='Arctic'):
        super().__init__(name, 'Penguin', diet=diet, biome=biome)

    def speak(self):
        return super().speak()


class Pheasant(Bird):
    def __init__(self, name):
        super().__init__(name, 'Pheasant')

    def speak(self):
        return super().speak()


class Peacock(Bird):
    def __init__(self, name):
        super().__init__(name, 'Peacock')

    def speak(self):
        return super().speak()