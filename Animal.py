'''
File: Animal.py
Description: This module contains the different animals as well as their characteristics
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
import Utilities

all_animals = []
meat_diet = []
plant_diet = []

class Animal(ABC):
    def __init__(self, name=None, species=None, age=0, diet=None, size=None, is_cold_blooded=False,
                 sound=None, biome=None, health=100):

        if name is None:
            self.name = Utilities.names
        else:
            self.name = name
        self.species = species
        self.age = age
        self.species = species
        self.age = age
        self.diet = diet
        self.size = size
        self.is_cold_blooded = is_cold_blooded
        self.sound = sound
        self.biome = biome
        self.health = health
        self.all_animals = all_animals
        self.meat_diet = meat_diet
        self.plant_diet = plant_diet

    animal_ID_index = 0
    animal_ID = f'{animal_ID_index:03d}'

    @abstractmethod
    def speak(self):
        pass

    @property
    @abstractmethod
    def is_predator(self):
        pass

    def get_description(self):
        return f'{self.ID}: {self.name} is a {self.age} year old {self.species}'

    # TODO Add animals with random names - Fine do to unique objects



    def add_animal(self, animal_object):
        '''Attempts to add an animal, running all checks.'''
        if animal_object.biome != self.biome:
            print(
                f'Couldn\'t add {animal_object.name}: Wrong Biome. Needs {animal_object.biome}, found {self.biome}.')
            return
        # TODO when adding new animal ensure there is an enclosure ready to move into with enough space
        if not self.check_size(animal_object):
            print(
                f'Failed to add {animal_object.name}: Not enough space (Required {animal_object.get_min_enclosure_area()}m²).')
            return
        #TODO Takes a day for animal to arrive,
        if not self.check_safety(animal_object):
            return

        all_animals.append(animal_object)
        print(f'{animal_object.name} the {animal_object.species} added to {self.name}.')
        #TODO assign ID to new animal and increment ID index
        self.animal_ID_index += 1



    # TODO Format health Records
    def health_record(self):
        CARD_WIDTH = 40
        print(f'________________________________________')
        name_and_age = f'Name: {self.name}    Age: {self.age}'
        print(f'|  {name_and_age:<{CARD_WIDTH - 5}}  |')
        species_info = f'Species: {self.species}'
        print(f'|  {species_info:<{CARD_WIDTH - 5}}  |')
        diet_info = f'Diet: {self.diet}'
        print(f'|  {diet_info:<{CARD_WIDTH - 5}}  |')
        health_info = f'Health Condition: {self.health}%'
        print(f'|  {health_info:<{CARD_WIDTH - 5}}  |')
        print(f'|  {"":<{CARD_WIDTH - 5}}  |')
        print(f'|_______________________________________|')

    def list_by_health(self):
        animals_sorted_by_health = sorted(self.all_animals,
                                          key= lambda animals: animals.health)
        for index, animal in enumerate(animals_sorted_by_health):
            print(f'{index + 1}. {animal.name} | Health: {animal.health}')

    def menu_remove_animal(self):
        print(self.all_animals)
        remove_animal = input('Which animal would you like to remove?')
        if remove_animal not in self.all_animals:
            print(f'\n{remove_animal} is not a valid animal.')
        else:
            self.all_animals.remove(remove_animal)


class Reptile(Animal):
    def __init__(self, name, species=None, age=0, diet='Meat', size=None, is_cold_blooded=True, sound=None, biome=None):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return 'Hiss'

    @property
    def is_predator(self):
        return True

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

    @property
    def is_predator(self):
        return True

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

    @property
    def is_predator(self):
        return True

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

    @property
    def is_predator(self):
        return False

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

    @property
    def is_predator(self):
        return True

class Ailuridae(Animal):
    def __init__(self, name, species=None, age=0, diet='Meat/Plants', size=.5, is_cold_blooded=False, sound=None,
                 biome='Jungle'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound

    @property
    def is_predator(self):
        return False

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

    @property
    def is_predator(self):
        return False

class Barracuda(Fish):
    def __init__(self, name, diet='Meat', size=1):
        super().__init__(name, 'Barracuda', diet=diet, size=size)

    def speak(self):
        return super().speak()

    @property
    def is_predator(self):
        return True

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

    @property
    def is_predator(self):
        return True

class PufferFish(Fish):
    def __init__(self, name, size=.2):
        super().__init__(name, 'Puffer Fish', size=size)

    def speak(self):
        return super().speak()


class Bird(Animal):
    def __init__(self, name, species=None, age=0, diet='Plants', size=.5, is_cold_blooded=False, sound='KACAAAW',
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound

    @property
    def is_predator(self):
        return False

class Penguin(Bird):
    def __init__(self, name, diet='Meat', biome='Arctic'):
        super().__init__(name, 'Penguin', diet=diet, biome=biome)

    def speak(self):
        return super().speak()

    @property
    def is_predator(self):
        return True

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
