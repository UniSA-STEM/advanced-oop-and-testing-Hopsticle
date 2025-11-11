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

all_staff = []
staff_responses = ['Yes?', 'What you want?', 'What...?', 'Me busy, leave me alone!', 'Me not that kind of orc!', 'Work, work',
                   'Okie Dokie', 'Something need doing?']

#TODO Start basic addition of staff and their roles
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
        pass

class Veterinarian(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Veterinarian')

    def speak(self):
        return 'Who\'s hurt?'

    def heal_animal(self, animal):
        pass

class Admin(Staff):
    def __init__(self, name=random.choice(names)):
        super().__init__(name, 'Admin')

    def speak(self):
        return random.choice(staff_responses)

#TODO implement actions that need to be undertaken by staff based on animal health and enclosure cleanliness

    def menu_list_all_staff(self):
        return all_staff

    def menu_list_by_job(self):
        pass

    def menu_staff_actions(self):
        '''clean, feed, heal'''
        pass

    def menu_add_staff(self):
        '''new staff, random choice name, append all staff'''
        pass

    def menu_remove_staff(self):
        '''remove staff from list'''
        pass
