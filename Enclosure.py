'''
File: Enclosure.py
Description: This module contains the permisible enclosure types for the animals ant their status
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


    #TODO ensure when creating multiple enclosures of the same biome there are no errors in overwriting existing - shouldn't unique objects

    def new_enclosure(self):
        all_enclosures.append(self)
        print(f'New enclosure added: {self.name}, it\'s a {self.biome} type with a size of {self.area}m²')
        return self
    #TODO new enclosure will take two days to build?

    def check_size(self, new_animal):
        '''Checks if the animal fits based on size rules.'''
        # Calculate current load
        all_occupants = self.animals + [new_animal]

        # Rule 1: Area must be 20x the largest animal
        largest_size = max(a.size for a in all_occupants)
        if self.area < (largest_size * 20):
            print(f"Refused: {new_animal.name} is too big for this enclosure.")
            return False

        # Rule 2: Area must be 5x combined size
        total_size = sum(a.size for a in all_occupants)
        if self.area < (total_size * 5):
            print(f"Refused: Enclosure too crowded for {new_animal.name}.")
            return False

        return True

    def check_safety(self, new_animal):
        '''Checks predator/prey compatibility.'''
        if not self.animals:
            return True # Safe if empty

        has_predator = any(a.is_predator for a in self.animals) or new_animal.is_predator
        has_prey = any(not a.is_predator for a in self.animals) or (not new_animal.is_predator)

        # If we have both predators and prey, it's unsafe
        if has_predator and has_prey:
            print(f"Refused: Safety Risk! Cannot mix Predators and Prey.")
            return False
        return True

    def add_animal(self, animal_object):
        if animal_object.biome != self.biome:
            print(f"Refused: {animal_object.name} needs {animal_object.biome}, this is {self.biome}.")
            return False

        if self.check_size(animal_object) and self.check_safety(animal_object):
            self.animals.append(animal_object)
            print(f"Success: {animal_object.name} added to {self.name}.")
            return True
        return False

    def get_occupants(self):
        if not self.animals:
            return f'The {self.name} has no animals'
        occupants = ','.join(f'{a.name}, {a.species}' for a in self.animals)
        return f'The {self.name} has {occupants} animals'

    def get_biome(self):
        return self.biome

    def get_cleanliness(self):
        return self.cleanliness
