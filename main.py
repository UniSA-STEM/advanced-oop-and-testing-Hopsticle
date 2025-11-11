'''
File: Staff.py
Description: This module contains the different staff roles and the individuals information
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random
import Staff
import Enclosure
import Animal
from abc import ABC, abstractmethod

all_animals = Animal.all_animals
all_staff = Staff.all_staff
all_enclosures = Enclosure.all_enclosures


print("Welcome to Zootopia\'s very own Zoo management tool")

def main():
    pass
    starting_selection = input('Would you like a '
          '\n1.Default,'
          '\n2.Randomised '
          '\n3.Custom zoo?')
    if starting_selection == '1':
        pass
        all_animals = []
        '''lion, penguin, red panda, barracuda, dingo'''
        all_staff = []
        '''Jesse, James, Ash'''
        all_enclosures = []
        '''savannah, arctic, jungle, water, brush'''
        pass
    elif starting_selection == '2':
        '''add 5 random animals with matching biome, and 3 staff'''
        pass
    else:
        animal_choice = input('How many animals would you like?')
        for animal in animal_choice:
            '''add random animals plus respective biomes/enclosurse'''
        staff_choice = input('How many staff would you like?')
        for staff in staff_choice:
            '''add random staff'''
        pass

    zoo_manager = ZooManager(all_animals, all_staff, all_enclosures)



#TODO implement main and zoom manager functions
class ZooManager:
    def __init__(self):
        self.all_animals = Animal.all_animals
        self.all_staff = Staff.all_staff
        self.all_enclosures = Enclosure.all_enclosures

        self.menu_items = ('---Main Menu---'
                           '\nAnimals'
                         '\nStaff'
                         '\nEnclosures')

        self.animal_menu = ('---Animals---'
                            '\nList All'
                            '\nList by Diet'
                            '\nList by '
                            '\nAnimal Health Card'
                            '\nAdd Animal'
                            '\nRemove Animal')

        self.staff_menu = ('---Staff---'
                           '\nList All'
                           '\nList by Job'
                           '\nStaff Actions'
                           '\nAdd Staff'
                           '\nRemove Staff')

        #TODO sort menu items by criteria
        self.enclosure_menu = ('---Enclosure---'
                               '\nList All'
                               '\nList by Biome'
                               '\nList by Cleanliness'
                               '\nAdd Enclosure'
                               '\nRemove Enclosure')

    def menu_main(self):
        print(self.menu_items)

    def menu_animals(self):
        pass

    def menu_list_all_animals(self):
        pass

    def menu_list_all_by_diet(self):
        pass

    def menu_health_card_menu(self):
        pass

    def menu_add_animal(self):
        pass

    def menu_remove_animal(self):
        pass

    def menu_staff(self):
        print(self.staff_menu)

    def menu_list_all_staff(self):
        pass

    def menu_list_by_job(self):
        pass

    def menu_staff_actions(self):
        pass

    def menu_add_staff(self):
        pass

    def menu_remove_staff(self):
        pass

    def enclosure_menu(self):
        print(self.enclosure_menu)

    def menu_list_all_enclosures(self):
        pass

    def menu_list_by_biome(self):
        pass

    def menu_list_by_cleanliness(self):
        pass

    def menu_add_enclosure(self):
        pass

    def menu_remove_enclosure(self):
        pass








go = ZooManager()
test = input("Would you like to add another animal? (Y/N) ")
if test == "Y":
    Animal.Animal.add_animal(Animal.Lion)



#TODO think of Extra functionality to add to project

#TODO Check overall encapsulation

if __name__ == '__main__':
    main()