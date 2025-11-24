'''
File: Enclosure.py
Description: This module contains the permissible enclosure types for the animals and their status.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

all_enclosures = []


class Enclosure:
    '''Represents an animal habitat with rules for size, safety, and cleanliness.'''
    
    biomes = ['Plains', 'Arctic', 'Jungle', 'Swamp', 'Savannah', 'Water', 'Forest', 'Brush']

    def __init__(self, name, biome: str, area: float, cleanliness=100):
        # --- Encapsulated Attributes (Protected) ---
        self._name = name
        self._biome = biome
        self._area = area
        self._cleanliness = cleanliness # Managed via a property setter/getter
        self._animals = [] # Protected list of Animal objects

    # -----------------------------------------------------------------
    # --- ENCAPSULATION PROPERTIES (Getters and Setters) ---
    # -----------------------------------------------------------------

    @property
    def name(self):
        '''Read-only access to the enclosure's name.'''
        return self._name

    @property
    def biome(self):
        '''Read-only access to the enclosure's biome type.'''
        return self._biome

    @property
    def area(self):
        '''Read-only access to the enclosure's area (m²).'''
        return self._area

    @property
    def animals(self):
        '''Provides read access to the list of animals in the enclosure.'''
        return self._animals

    @property
    def cleanliness(self):
        '''Getter for the enclosure's cleanliness level (0-100).'''
        return self._cleanliness

    @cleanliness.setter
    def cleanliness(self, value):
        '''Setter for cleanliness, ensuring the value stays within the 0-100 range.'''
        if 0 <= value <= 100:
            self._cleanliness = value
        elif value < 0:
            self._cleanliness = 0
        else:
            self._cleanliness = 100

    # -----------------------------------------------------------------
    # --- Methods (Updated to use encapsulated data) ---
    # -----------------------------------------------------------------

    def __str__(self):
        # Uses properties for consistent display
        return (f'Enclosure: {self.name}'
                f'\nBiome: {self.biome}'
                f'\nAnimals: {[a.name for a in self.animals]}' # Using self.animals property
                f'\nCleanliness: {self.cleanliness}') # Using self.cleanliness property

    def new_enclosure(self):
        '''Registers the new enclosure and prints a confirmation message.'''
        all_enclosures.append(self)
        # Using protected attributes (or properties) for output
        print(f'New enclosure added: {self._name}, it\'s a {self._biome} type with a size of {self._area}m²')
        return self

    def check_size(self, new_animal):
        '''Checks if the animal fits based on total size rules, returning status and message.'''
        total_animal_size = sum(a.size for a in self.animals)
        new_total_size = total_animal_size + new_animal.size
        
        # Using self._area (or self.area property)
        if new_total_size > self._area: 
            return False, f'Refused: The enclosure is too crowded for {new_animal.name}.'

        return True, None

    def check_safety(self, new_animal):
        '''Checks predator/prey compatibility, returning status and message.'''
        # Using self.animals property
        if not self.animals:
            return True, None # Safe if empty

        # Check existing animals using self.animals property
        has_predator = any(a.is_predator for a in self.animals) or new_animal.is_predator
        has_prey = any(not a.is_predator for a in self.animals) or (not new_animal.is_predator)

        # If we have both predators and prey, it's unsafe
        if has_predator and has_prey:
            return False, 'Safety Risk! Cannot mix Predators and Prey.'
        return True, None

    def add_animal(self, animal_object):
        '''Attempts to add an animal after checking biome, size, and safety. Returns status and message.'''
        
        # Check 1: Biome (using self.biome property)
        if animal_object.biome != self.biome:
            return False, f'Refused: {animal_object.name} needs {animal_object.biome}, this is {self.biome}.'

        # Check 2 & 3: Size and Safety
        size_ok, size_message = self.check_size(animal_object)
        if not size_ok:
            return False, size_message

        safety_ok, safety_message = self.check_safety(animal_object)
        if not safety_ok:
            return False, safety_message

        # All checks passed
        self._animals.append(animal_object) # Direct modification of the protected list
        # Using self.name property
        return True, f'Success: {animal_object.name} added to {self.name}.'

    def get_occupants(self):
        '''Returns a string listing the names of animals in the enclosure.'''
        if not self.animals: # Uses self.animals property
            # Uses self.name property
            return f'The {self.name} has no animals'
            
        # Uses self.animals property
        occupants = ', '.join(f'{a.name} the {a.species}' for a in self.animals) 
        # Uses self.name property
        return f'The {self.name} currently holds: {occupants}'