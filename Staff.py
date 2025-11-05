'''
File: Staff.py
Description: This module contains the different staff roles and the individuals information
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random

def load_names(filename='Names'):
#Load file used to generate Staff names
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []
names = load_names()

#TODO Start basic addition of staff and their roles
class Staff:
    def __init__(self, function=None, name=random.choice(names)):
        self.name = name
        self.function = function

    def __str__(self):
        return self.name

class Zookepper(Staff):
    def __init__(self, function=None, name=random.choice(names)):
        super().__init__(function, name)

class Vetranarian(Staff):
    def __init__(self, function=None, name=random.choice(names)):
        super().__init__(function, name)

class Admin(Staff):
    def __init__(self, function=None, name=random.choice(names)):
        super().__init__(function, name)

#TODO implement actions that need to be undertaken by staff based on animal health and enclosure cleanliness

print(names)
staff = Staff()