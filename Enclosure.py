'''
File: Enclosure.py
Description: This module contains the permisible enclosure types for the animals ant their status
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

all_enclosures = []
biomes = ['Plains', 'Arctic', 'Jungle', 'Swamp', 'Savannah', 'Water', 'Forest', 'Brush']
import Animal

class Enclosure:
    def __init__(self, name, biome: str, area: float, cleanliness=100):
        self.name = name
        self.biome = biome
        self.area = area
        self.cleanliness = cleanliness
        self.animals = []

    def __str__(self):
        return (f'Enclosure: {self.name}'
                f'\nBiome: {self.biome}'
                f'\nAnimals: {self.animals}')


    #TODO ensure when creating multiple enclosures of the same biome there are no errors in overwriting existing - shouldn't unique objects

    def new_enclosure(self):
        all_enclosures.append(self)
        print(f'New enclosure added: {self.name}, it\'s a {self.biome} type with a size of {self.area}m²')
        return self
    #TODO new enclosure will take two days to build?

    def check_size(self, new_animal):
        '''Enforces two size requirements:
        1. Area must be 20x the largest animal's size.
        2. Area must be 5x the total combined size of all occupants.'''
        #TODO implement size requirements for enclosure based on animal size
        all_occupants = self.animals + [new_animal]
        largest_animal_size = max(a.size for a in all_occupants)
        min_area_individual = largest_animal_size * 20

        if self.area < min_area_individual:
            print(
                f'Size Fail (Rule 1): Area ({self.area}m²) is too small for the largest animal (Size: {largest_animal_size}m).'
                f' Needs at least {min_area_individual}m².')
            return False

        total_combined_size = sum(a.size for a in all_occupants)
        min_area_occupancy = total_combined_size * 5

        if self.area < min_area_occupancy:
            print(
                f'Size Fail (Rule 2): Area ({self.area}m²) is too small. Combined size: {total_combined_size}m.'
                f' Needs at least {min_area_occupancy}m².')
            return False

        return True

    def check_safety(self, new_animal):
        '''Enforces safety rules: Predators cannot be mixed with non-predators, except fish.'''
        all_occupants = self.animals + [new_animal]
        has_predator = any(a.is_predator for a in all_occupants)
        has_non_predator = any(not a.is_predator for a in all_occupants)

        if has_predator and has_non_predator:
            are_all_fish = all(isinstance(a, Animal.Fish) for a in all_occupants)
            if not are_all_fish:
                pred_example = next((a.species for a in all_occupants if a.is_predator), 'Predator')
                non_pred_example = next((a.species for a in all_occupants if not a.is_predator), 'Non-Predator')
                print(
                    f'Cannot mix predator ({pred_example}) with non-predator ({non_pred_example}).')
                return False
            return True
        return True

    def add_animal(self, animal_object):
        '''Attempts to add an animal, running all checks.'''
        if animal_object.biome != self.biome:
            print(
                f'Failed to add {animal_object.name}: Biome mismatch. Needs {animal_object.biome}, found {self.biome}.')
            return

        if not self.check_size(animal_object):
            print(
                f'Failed to add {animal_object.name}: Not enough space.')
            return

        if not self.check_safety(animal_object):
            return

        self.animals.append(animal_object)
        print(f'{animal_object.name} the {animal_object.species} added to {self.name}.')

    def get_occupants(self):
        if not self.animals:
            return f'The {self.name} has no animals'
        occupants = ','.join(f'{a.name}, {a.species}' for a in self.animals)
        return f'The {self.name} has {occupants} animals'

    def get_biome(self):
        return self.biome

    def get_cleanliness(self):
        return self.cleanliness
