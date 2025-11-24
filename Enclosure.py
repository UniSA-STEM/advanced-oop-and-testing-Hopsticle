'''
File: Enclosure.py
Description: This module contains the permissible enclosure types for the animals and their status
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

all_enclosures = []


class Enclosure:
    biomes = ['Plains', 'Arctic', 'Jungle', 'Swamp', 'Savannah', 'Water', 'Forest', 'Brush']

    def __init__(self, name, biome: str, area: float, cleanliness=100):
        self.name = name
        self.biome = biome
        self.area = area
        self.cleanliness = cleanliness
        self.animals = []

    def __str__(self):
        return (f'Enclosure: {self.name}'
                f'\nBiome: {self.biome}'
                f'\nAnimals: {self.animals}'
                f'\nCleanliness: {self.cleanliness}')

    def new_enclosure(self):
        all_enclosures.append(self)
        print(f'New enclosure added: {self.name}, it\'s a {self.biome} type with a size of {self.area}m²')
        return self

    # TODO when adding new enclosure, check to see if name already exists

    def check_size(self, new_animal):
        '''Checks if the animal fits based on size rules.'''
        # Calculate current load
        all_occupants = self.animals + [new_animal]

        # Rule 1: Area must be 20x the largest animal
        largest_size = max(a.size for a in all_occupants)
        if self.area < (largest_size * 20):
            # Change print to return (False, reason)
            return False, f'{new_animal.name} is too big for this enclosure.'

        # Rule 2: Area must be 5x combined size
        total_size = sum(a.size for a in all_occupants)
        if self.area < (total_size * 5):
            # Change print to return (False, reason)
            return False, f'Enclosure too crowded for {new_animal.name}.'

        return True, None  # Return True and None for no message

    # Update check_safety to return status and message
    def check_safety(self, new_animal):
        '''Checks predator/prey compatibility.'''
        if not self.animals:
            return True, None  # Safe if empty

        has_predator = any(a.is_predator for a in self.animals) or new_animal.is_predator
        has_prey = any(not a.is_predator for a in self.animals) or (not new_animal.is_predator)

        # If we have both predators and prey, it's unsafe
        if has_predator and has_prey:
            # Change print to return (False, reason)
            return False, 'Safety Risk! Cannot mix Predators and Prey.'
        return True, None

    # Update add_animal to consolidate and return status and message
    def add_animal(self, animal_object):
        # Check 1: Biome
        if animal_object.biome != self.biome:
            # Change print to return (False, reason)
            return False, f'{animal_object.name} needs {animal_object.biome}, this is {self.biome}.'

        # Check 2 & 3: Size and Safety (using updated methods)
        size_ok, size_message = self.check_size(animal_object)
        if not size_ok:
            return False, size_message

        safety_ok, safety_message = self.check_safety(animal_object)
        if not safety_ok:
            return False, safety_message

        # All checks passed
        self.animals.append(animal_object)
        # Change print to return (True, message)
        return True, f'Success: {animal_object.name} added to {self.name}.'

    def get_occupants(self):
        if not self.animals:
            return f'The {self.name} has no animals'
        occupants = ', '.join(f'{a.name}' for a in self.animals)

        return f'The {self.name} has {occupants}.'

    def get_biome(self):
        return self.biome

    def get_cleanliness(self):
        return self.cleanliness
