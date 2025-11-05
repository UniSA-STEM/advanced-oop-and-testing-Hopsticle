'''
File: Enclosure.py
Description: This module contains the permisible enclosure types for the animals ant their status
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

enclosures = []
environments = ['Plains', 'Arctic', 'Jungle', 'Swamp', 'Savannah', 'Water', 'Forest', 'Brush']

#TODO implement size requirements for enclosure based on animal size
class Enclosure:
    def __init__(self, name, environment: str, area: float, cleanliness=100):
        self.name = name
        self.environment = environment
        self.area = area
        self.cleanliness = cleanliness
        self.animals = []

    def new_enclosure(self):
        add_enclosure = Enclosure(self.name, self.environment, self.cleanliness, self.size)
        enclosures.append(add_enclosure)
        print(f'New enclosure added to {self.name}, it\'s is a {self.environment} type with a size of {self.size}')
        return add_enclosure

    def check_size(self, new_animal):
        """
        Enforces two size requirements:
        1. Area must be 20x the largest animal's size.
        2. Area must be 5x the total combined size of all occupants.
        """

        all_occupants = self.animals + [new_animal]

        largest_animal_size = max(a.size for a in all_occupants)
        min_area_individual = largest_animal_size * 20

        if self.area < min_area_individual:
            print(
                f"Size Fail (Rule 1): Area ({self.area}m²) is too small for the largest animal (Size: {largest_animal_size}m)."
                f" Needs at least {min_area_individual}m².")
            return False

        total_combined_size = sum(a.size for a in all_occupants)
        min_area_occupancy = total_combined_size * 5

        if self.area < min_area_occupancy:
            print(
                f"Size Fail (Rule 2): Area ({self.area}m²) is too small. Combined size: {total_combined_size}m."
                f" Needs at least {min_area_occupancy}m².")
            return False

        return True

class Environment(Enclosure):
    def __init__(self, name, environment =None):
        super().__init__(name, environment)

class SizeEnclosure(Enclosure):
    def __init__(self, name, size=None):
        Enclosure.__init__(self, name, size)


class Cleanliness(Enclosure):
    def __init__(self, name, cleanliness=100):
        Enclosure.__init__(self, name, cleanliness)

    def check_size(self, new_animal):
        """Checks if the enclosure has enough space for the new animal."""
        current_required_area = sum(a.get_min_enclosure_area() for a in self.animals)

        required_for_new_animal = new_animal.get_min_enclosure_area()

        if self.area >= current_required_area + required_for_new_animal:
            return True
        else:
            return False

#TODO ensure enclosures do not have carnivores with other types of animals, except maybe fish?

#TODO List of all animals within one enclosure work on display and naming convention for enclosures

    def add_animal(self, animal_object):
        '''Attempts to add an animal, running all checks.'''
        if animal_object.biome != self.environment:
            print(
                f'Failed to add {animal_object.name}: Biome mismatch. Needs {animal_object.biome}, found {self.environment}.')
            return

        if not self.check_size(animal_object):
            print(
                f'Failed to add {animal_object.name}: Not enough space (Required {animal_object.get_min_enclosure_area()}m²).')
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

    def get_enclosure_type(self):
        return self.environment