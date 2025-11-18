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

import Animal
import Enclosure

def load_names(filename='Names'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []
names = load_names()

all_staff = []
staff_responses = ['Yes?', 'What you want?', 'What...?', 'Me busy, leave me alone!', 'Me not that kind of orc!',
                   'Work, work', 'Okie Dokie', 'Something need doing?']

class Staff(ABC):
    def __init__(self, name=random.choice(names), function=None):
        self.name = name
        self.function = function


    @abstractmethod
    def speak(self):
        pass

    def __str__(self):
        return f'{self.name} is a {self.function}'


class Zookeeper(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Zookeeper')

    def speak(self):
        return random.choice(staff_responses)

    def clean_enclosure(self):
        self.list_by_cleanliness(self.name)
        clean = input('Which enclosure should be cleaned?')
        pass

#TODO implement actions that need to be undertaken by staff based on animal health and enclosure cleanliness

class Veterinarian(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Veterinarian')

    def speak(self):
        return 'Who\'s hurt?'

    def heal_animal(self, animal):
        Animal.Animal.list_by_health(self.name)
        heal = input('Which animal should be healed?')
        pass

#TODO one admin required for each other 4 staff, just because why not..? they do nothing really ;)
class Admin(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Admin')

    def speak(self):
        return random.choice(staff_responses)