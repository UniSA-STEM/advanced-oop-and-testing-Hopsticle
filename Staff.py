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

#Utilities imports is needed for interaction/utility functions
import Utilities

all_staff = []
staff_responses = ['Yes?', 'What you want?', 'What...?', 'Me busy, leave me alone!', 'Me not that kind of orc!',
                   'Work, work', 'Okie Dokie', 'Something need doing?']


class Staff(ABC):
    '''Abstract base class for all staff members.'''

    def __init__(self, name=None, function=None):

        # --- Encapsulated Attributes (Protected) ---
        if name is None:
            self._name = Utilities.get_random_name()
        else:
            self._name = name

        self._function = function # The role (e.g., Zookeeper, Veterinarian)

    # -----------------------------------------------------------------
    # --- ENCAPSULATION PROPERTIES (Getters) ---
    # -----------------------------------------------------------------

    @property
    def name(self):
        '''Getter: Provides read-only access to the staff member's name.'''
        return self._name

    @property
    def function(self):
        '''Getter: Provides read-only access to the staff member's role.'''
        return self._function

    # -----------------------------------------------------------------
    # --- Abstract Methods ---
    # -----------------------------------------------------------------

    @abstractmethod
    def speak(self):
        '''Requires all subclasses to implement a specific speaking behavior.'''
        pass

    def __str__(self):
        # Uses properties for consistent display
        return f'{self.name} is a {self.function}'


# -----------------------------------------------------------------
# --- CONCRETE STAFF CLASSES ---
# -----------------------------------------------------------------

class Zookeeper(Staff):
    '''Handles daily maintenance tasks like feeding and cleaning.'''

    def __init__(self, name=None):
        super().__init__(name, 'Zookeeper') # Sets the protected _function attribute

    def speak(self):
        return random.choice(staff_responses)

    def feed_animals(self, enclosure):
        '''Simulates feeding all animals in a given enclosure.'''
        # Uses enclosure.animals property (from Enclosure module) for checks
        if not enclosure.animals:
            return f'There are no animals in {enclosure.name} to feed.'

        # Uses self.name property (from Staff base class)
        return f'{self.name} the Zookeeper fed all {len(enclosure.animals)} animals in {enclosure.name}.'

    def clean_enclosure(self, enclosure):
        '''Sets the enclosure cleanliness to 100.'''
        # Uses enclosure.cleanliness property setter (from Enclosure module)
        enclosure.cleanliness = 100
        # Uses self.name property (from Staff base class)
        return f'{self.name} the Zookeeper successfully cleaned {enclosure.name}. Cleanliness is now 100.'


class Veterinarian(Staff):
    '''Handles medical tasks like healing sick animals.'''

    def __init__(self, name=None):
        super().__init__(name, 'Veterinarian') # Sets the protected _function attribute

    def speak(self):
        return 'Who\'s hurt?'

    def heal_animal(self, animal):
        '''Sets an animal's health to 100.'''
        # Uses animal.health property getter (from Animal module)
        if animal.health == 100:
            return f'{self.name} checked {animal.name} and found them perfectly healthy. No action needed.'

        # Uses animal.health property setter (from Animal module)
        animal.health = 100
        # Uses self.name property (from Staff base class) and animal.name property
        return f'{self.name} the Veterinarian healed {animal.name}. Health is now 100.'


class Admin(Staff):
    '''Represents the management role.'''

    def __init__(self, name=None):
        super().__init__(name, 'Admin') # Sets the protected _function attribute

    def speak(self):
        return 'The zoo is operational.'