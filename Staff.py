'''
File: Staff.py
Description: This module contains the different staff roles and the individuals information
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random
from abc import ABC, abstractmethod

def load_names(filename='Names'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []
names = load_names()

#TODO Start basic addition of staff and their roles
class Staff(ABC):
    def __init__(self, name=random.choice(names), function=None, sound=None):
        self.name = name
        self.function = function
        self.sound = sound

    @abstractmethod
    def speak(self):
        return 'How can I Help?'

    def __str__(self):
        return f'{self.name} is a {self.function}'


class Zookeeper(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Zookeeper')

    def speak(self):
        return super().speak()

class Veterinarian(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Veterinarian')

    def speak(self):
        return super().speak()

class Admin(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Admin')

    def speak(self):
        return super().speak()

#TODO implement actions that need to be undertaken by staff based on animal health and enclosure cleanliness

print(names)
staff = Staff()