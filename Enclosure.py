'''
File: Staff.py
Description: This module contains the permisible enclosure types for the animals ant their status
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

enclosures = []
environments = ['Plains', 'Arctic', 'Jungle', 'Swamp', 'Savannah', 'Water', 'Forest', 'Brush']

#TODO implement size requirments for enclosure based on animal size
class Enclosure:
    def __init__(self, name, environment =None, cleanliness=100, size=None):
        self.name = name
        self.environment = environment
        self.cleanliness = cleanliness
        self.size = size

    def new_enclosure(self):
        add_enclosure = Enclosure(self.name, self.environment, self.cleanliness, self.size)
        enclosures.append(add_enclosure)
        print(f'New enclosure added to {self.name}, it\'s is a {self.environment} type with a size of {self.size}')
        return add_enclosure

class Environment(Enclosure):
    def __init__(self, name, environment =None):
        super().__init__(name, environment)

class SizeEnclosure(Enclosure):
    def __init__(self, name, size=None):
        Enclosure.__init__(self, name, size)


class Cleanliness(Enclosure):
    def __init__(self, name, cleanliness=100):
        Enclosure.__init__(self, name, cleanliness)

#TODO ensure enclosures do not have carnivores with other types of animals, except maybe fish?

#TODO List of all animals within one enclosure work on display and naming convention for enclosures

