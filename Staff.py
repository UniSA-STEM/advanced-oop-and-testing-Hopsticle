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
import Utilities

all_staff = []
staff_responses = ['Yes?', 'What you want?', 'What...?', 'Me busy, leave me alone!', 'Me not that kind of orc!',
                   'Work, work', 'Okie Dokie', 'Something need doing?']


class Staff(ABC):
    def __init__(self, name=None, function=None):

        if name is None:
            self.name = Utilities.get_random_name()
        else:
            self.name = name
        self.function = function

    @abstractmethod
    def speak(self):
        pass

    def __str__(self):
        return f'{self.name} is a {self.function}'


class Zookeeper(Staff):
    def __init__(self, name=None):
        super().__init__(name, 'Zookeeper')

    def speak(self):
        return random.choice(staff_responses)

    def feed_animals(self, enclosure):
        '''Sets the 'fed' status for all animals in the enclosure'''
        if not enclosure.animals:
            return f'There are no animals in {enclosure.name} to feed.'

        return f'{self.name} the Zookeeper fed all {len(enclosure.animals)} animals in {enclosure.name}.'

    def clean_enclosure(self, enclosure):
        '''Sets the enclosure cleanliness to 100'''
        enclosure.cleanliness = 100
        return f'{self.name} the Zookeeper successfully cleaned {enclosure.name}. Cleanliness is now 100.'


class Veterinarian(Staff):
    def __init__(self, name=None):
        super().__init__(name, 'Veterinarian')

    def speak(self):
        return 'Who\'s hurt?'

    def heal_animal(self, animal):
        '''Sets the animal health to 100.'''
        if animal.health == 100:
            return f'{self.name} checked {animal.name} and found them perfectly healthy. No action needed.'

        animal.health = 100
        return f'{self.name} the Veterinarian healed {animal.name}. Health is now 100.'


class Admin(Staff):
    def __init__(self, name=None):
        super().__init__(name, 'Admin')

    def speak(self):
        return random.choice(staff_responses)

    def do_things(self):
        pass
