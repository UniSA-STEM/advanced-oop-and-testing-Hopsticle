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

# Global lists
all_animals = []
meat_diet = []
plant_diet = []

class Animal(ABC):
    '''
    Abstract Base Class for all animals in the zoo.
    Enforces abstract methods (speak, is_predator) that must be implemented by subclasses.
    '''
    _next_id = 1 # Class variable for generating unique animal IDs

    def __init__(self, name=None, species=None, age=0, diet=None, size=None, is_cold_blooded=False,
                 sound=None, biome=None, health=100):

        # Generate unique animal ID (e.g., A001, A002)
        self._animal_id = f'A{Animal._next_id:03d}'
        Animal._next_id += 1

        # Set name (uses a random name if none provided)
        if name is None:
            self._name = Utilities.get_random_name()
        else:
            self._name = name
            
        # Initialize core animal attributes
        self._species = species
        self._age = age
        self._diet = diet
        self._size = size
        self._is_cold_blooded = is_cold_blooded
        self._sound = sound
        self._biome = biome
        self.health = health # Uses the setter for validation
        
        # Assign global lists as instance attributes (note: this just creates references to the global lists)
        self.all_animals = all_animals
        self.meat_diet = meat_diet
        self.plant_diet = plant_diet

    # --- Property Getters (Read-Only Access) ---

    @property
    def animal_id(self):
        # Provides read-only access to the animal's unique ID.
        return self._animal_id

    @property
    def name(self):
        # Provides read access to the animal's name.
        return self._name

    @property
    def species(self):
        # Provides read access to the animal's species.
        return self._species

    @property
    def age(self):
        # Provides read access to the animal's age.
        return self._age

    @property
    def diet(self):
        # Provides read access to the animal's diet type.
        return self._diet

    @property
    def size(self):
        # Provides read access to the animal's volume.
        return self._size

    @property
    def is_cold_blooded(self):
        # Provides read access to the animal's cold-blooded status.
        return self._is_cold_blooded

    @property
    def sound(self):
        # Provides read access to the characteristic sound the animal makes.
        return self._sound

    @property
    def biome(self):
        # Provides read access to the animal's required environment/biome.
        return self._biome

    @property
    def health(self):
        # Provides read access to the animal's current health percentage.
        return self._health

    # --- Health Setter (With Validation) ---

    @health.setter
    def health(self, value):
        # Allows health to be modified while clamping the value between 0 and 100.
        self._health = max(0, min(100, value))

    # --- Abstract Methods (Must be implemented by concrete subclasses) ---

    @abstractmethod
    def speak(self):
        '''Returns the characteristic sound the animal makes.'''
        pass

    @property
    @abstractmethod
    def is_predator(self):
        '''Returns True if the animal is a predator, False otherwise.'''
        pass

    # --- Instance Methods ---

    def get_description(self):
        '''Returns a basic descriptive string of the animal.'''
        return f'{self.animal_id}: {self.name} is a {self.age} year old {self.species}'

    def health_record(self):
        '''Prints a formatted health card with key animal details.'''
        CARD_WIDTH = 40
        name_and_age = f'Name: {self.name}    Age: {self.age}'
        species_info = f'Species: {self.species}'
        diet_info = f'Diet: {self.diet}'
        health_info = f'Health Condition: {self.health}%'
        animal_cry = f'"{self.speak()}"'

        # Print the formatted health card
        print(f' _______________________________________')
        print(f'|  {name_and_age:<{CARD_WIDTH - 5}}  |')
        print(f'|  {species_info:<{CARD_WIDTH - 5}}  |')
        print(f'|  {diet_info:<{CARD_WIDTH - 5}}  |')
        print(f'|  {health_info:<{CARD_WIDTH - 5}}  |')
        print(f'|  {animal_cry :<{CARD_WIDTH - 5}}  |')
        print(f'|_______________________________________|')

    def list_by_health(self):
        '''Sorts and prints all animals (using the global list) by their current health.'''
        # Sort animals based on the health attribute
        animals_sorted_by_health = sorted(self.all_animals,
                                          key= lambda animals: animals.health)
        for index, animal in enumerate(animals_sorted_by_health):
            print(f'{index + 1}. {animal.name} | Health: {animal.health}')

    # --- Class Method ---

    @classmethod
    def get_all_concrete_animal_types(cls):
        '''Finds and returns the names of all non-abstract classes that inherit from Animal.'''
        all_classes = []
        # Iterate over immediate subclasses
        for base_class in cls.__subclasses__():
            # Iterate over concrete subclasses
            for concrete_class in base_class.__subclasses__():
                all_classes.append(concrete_class.__name__)
        return sorted(all_classes)


# --- Subclasses defining Animal groups and species ---

class Reptile(Animal):
    '''Base class for cold-blooded, meat-eating reptiles (default).'''
    def __init__(self, name, species=None, age=0, diet='Meat', size=None, is_cold_blooded=True, sound=None, biome=None):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return 'Hiss'

    @property
    def is_predator(self):
        return True # Default for reptiles


class Crocodile(Reptile):
    '''A specific type of Reptile with default attributes.'''
    def __init__(self, name, size=3, biome='Swamp'):
        super().__init__(name, 'Crocodile', size=size, biome=biome)

    def speak(self):
        return 'Beeeeellollolloloow'


class Snake(Reptile):
    '''A specific type of Reptile with default attributes.'''
    def __init__(self, name, size=1.5, biome='Forest'):
        super().__init__(name, 'Snake', size=size, biome=biome)

    def speak(self):
        return super().speak() + 'sssss' # Overrides speak to add 'sssss' to 'Hiss'


class Iguana(Reptile):
    '''A specific type of Reptile with default attributes.'''
    def __init__(self, name, size=1, biome='Brush'):
        super().__init__(name, 'Iguana', size=size, biome=biome)

    def speak(self):
        return super().speak()


class Turtle(Reptile):
    '''A specific type of Reptile (Herbivore) with default attributes.'''
    def __init__(self, name, diet='Plants', size=1, biome='Water'):
        # Overrides the default 'Meat' diet from Reptile
        super().__init__(name, 'Turtle', diet=diet, size=size, biome=biome)

    def speak(self):
        return super().speak()


class Feline(Animal):
    '''Base class for warm-blooded, meat-eating felines.'''
    def __init__(self, name, species=None, age=0, diet='Meat', size=2, is_cold_blooded=False, sound=None,
                 biome='Jungle'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return 'ROOOARRR'

    @property
    def is_predator(self):
        return True # Default for felines


class Lion(Feline):
    '''A specific type of Feline, setting Savannah biome.'''
    def __init__(self, name, biome='Savannah'):
        super().__init__(name, 'Lion', biome=biome)

    def speak(self):
        return super().speak()


class Tiger(Feline):
    '''A specific type of Feline.'''
    def __init__(self, name):
        super().__init__(name, 'Tiger')

    def speak(self):
        return super().speak()


class Panther(Feline):
    '''A specific type of Feline.'''
    def __init__(self, name):
        super().__init__(name, 'Panther')

    def speak(self):
        return super().speak()


class Canine(Animal):
    '''Base class for warm-blooded, meat-eating canines.'''
    def __init__(self, name, species=None, age=0, diet='Meat', size=None, is_cold_blooded=False, sound=None,
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        # Uses the sound attribute set in subclasses
        return self.sound

    @property
    def is_predator(self):
        return True # Default for canines


class Dingo(Canine):
    '''A specific type of Canine.'''
    def __init__(self, name, size=1):
        super().__init__(name, 'Dingo', size=size)

    def speak(self):
        return 'Wooof'


class Wolf(Canine):
    '''A specific type of Canine, setting Forest biome.'''
    def __init__(self, name, size=1.5, biome='Forest'):
        super().__init__(name, 'Wolf', size=size, biome=biome)

    def speak(self):
        return 'Hoooowwlllll'


class FennecFox(Canine):
    '''A specific type of Canine.'''
    def __init__(self, name, size=.5):
        super().__init__(name, 'Fennec Fox', size=size)

    def speak(self):
        return 'Yip'


class Marsupial(Animal):
    '''Base class for warm-blooded, plant-eating marsupials (default).'''
    def __init__(self, name, species=None, age=0, diet='Plants', size=None, is_cold_blooded=False, sound=None,
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        # Uses the sound attribute set in subclasses
        return self.sound

    @property
    def is_predator(self):
        return False # Default for marsupials


class Kangaroo(Marsupial):
    '''A specific type of Marsupial.'''
    def __init__(self, name, size=1.5):
        super().__init__(name, 'Kangaroo', size=size)

    def speak(self):
        return 'Booiiiing'


class Bilby(Marsupial):
    '''A specific type of Marsupial.'''
    def __init__(self, name, size=.5):
        super().__init__(name, 'Bilby', size=size)

    def speak(self):
        return 'Tck tck'


class TasmanianDevil(Marsupial):
    '''A specific type of Marsupial (Carnivore) which is a predator.'''
    def __init__(self, name, size=.5):
        # Overrides the default 'Plants' diet from Marsupial
        super().__init__(name, 'Tasmanian Devil', diet='Meat', size=size)

    def speak(self):
        return 'SCCREEEEEEEEE'

    @property
    def is_predator(self):
        return True # Overrides the default False from Marsupial


class Ailuridae(Animal):
    '''Base class for Red Panda family (Herbivore).'''
    def __init__(self, name, species=None, age=0, diet='Plants', size=.5, is_cold_blooded=False, sound='Squeak',
                 biome='Jungle'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound

    @property
    def is_predator(self):
        return False # Default for Ailuridae


class RedPanda(Ailuridae):
    '''A specific type of Ailuridae.'''
    def __init__(self, name):
        super().__init__(name, 'Red Panda')

    def speak(self):
        return super().speak()


class Fish(Animal):
    '''Base class for cold-blooded aquatic life.'''
    def __init__(self, name, species=None, age=0, diet='Plants', size=None, is_cold_blooded=True, sound='Glub Glub',
                 biome='Water'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound

    @property
    def is_predator(self):
        return False # Default for Fish


class Barracuda(Fish):
    '''A specific type of Fish (Carnivore) which is a predator.'''
    def __init__(self, name, diet='Meat', size=1):
        # Overrides the default 'Plants' diet from Fish
        super().__init__(name, 'Barracuda', diet=diet, size=size)

    def speak(self):
        return super().speak()

    @property
    def is_predator(self):
        return True # Overrides the default False from Fish


class ClownFish(Fish):
    '''A specific type of Fish.'''
    def __init__(self, name, size=.2):
        super().__init__(name, 'Clown Fish', size=size)

    def speak(self):
        return super().speak()


class Piranha(Fish):
    '''A specific type of Fish (Carnivore) which is a predator.'''
    def __init__(self, name, diet='Meat', size=.2):
        # Overrides the default 'Plants' diet from Fish
        super().__init__(name, 'Piranha', diet=diet, size=size)

    def speak(self):
        return super().speak()

    @property
    def is_predator(self):
        return True # Overrides the default False from Fish


class PufferFish(Fish):
    '''A specific type of Fish.'''
    def __init__(self, name, size=.2):
        super().__init__(name, 'Puffer Fish', size=size)

    def speak(self):
        return super().speak()


class Bird(Animal):
    '''Base class for warm-blooded birds.'''
    def __init__(self, name, species=None, age=0, diet='Plants', size=.5, is_cold_blooded=False, sound='KACAAAW',
                 biome='Brush'):
        super().__init__(name, species, age, diet, size, is_cold_blooded, sound, biome)

    def speak(self):
        return self.sound

    @property
    def is_predator(self):
        return False # Default for Bird


class Penguin(Bird):
    '''A specific type of Bird (Carnivore) which is a predator, setting Arctic biome.'''
    def __init__(self, name, diet='Meat', biome='Arctic'):
        # Overrides the default 'Plants' diet from Bird
        super().__init__(name, 'Penguin', diet=diet, biome=biome)

    def speak(self):
        return super().speak()

    @property
    def is_predator(self):
        return True # Overrides the default False from Bird


class Pheasant(Bird):
    '''A specific type of Bird.'''
    def __init__(self, name):
        super().__init__(name, 'Pheasant')

    def speak(self):
        return super().speak()


class Peacock(Bird):
    '''A specific type of Bird.'''
    def __init__(self, name):
        super().__init__(name, 'Peacock')

    def speak(self):
        return super().speak()