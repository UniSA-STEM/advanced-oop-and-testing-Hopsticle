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

print("Welcome to Zootopia ")

all_staff = []
# def main():
#     add_staff = Staff.Staff(name=random.choice(Staff.names))
#     all_staff.append(add_staff)
#
#     print(all_staff)
#
# class ZooManager():
#     def __init__(self, all_staff):
#         self.staff = all_staff
#
#     def add_staff(self):
#         new_staff = Staff.Staff(name=random.choice(Staff.names))
#         print(new_staff)
#         all_staff.append(new_staff)
#
# ZooManager(all_staff)

#TODO implement main and zoom manager functions
class ZooManager:
    def __init__(self):
        self.all_animals = Animal.all_animals

        self.menu_items = ('---Main Menu---'
                         '\nAnimals'
                         '\nStaff'
                         '\nEnclosures')

        self.animal_menu = ('---Animals---'
                            '\nList All'
                            '\nList by Diet'
                            '\nList by '
                            '\nAnimal Health Card')

        self.staff_menu = ('---Staff---'
                           '\nList All'
                           '\nList by Job'
                           '\nStaff Actions')

        self.enclosure_menu = ('---Enclosure---'
                               '\nList All'
                               '\nList by Biome'
                               '\nList by Cleanliness')


    def add_animal(self, animal_object):
        if not isinstance(animal_object, Animal) or type(animal_object) is Animal:
            print("Error: Cannot add an abstract Animal or non-Animal object.")
            return

        self.all_animals.append(animal_object)
        print(f"New animal added: {animal_object.name} the {animal_object.species}!")

    def list_animals_by_biome(self, target_biome):
        print(f"\n--- Animals in the {target_biome} Enclosure ---")
        found = [animal for animal in self.all_animals if animal.biome == target_biome]

        if not found:
            print(f"No animals currently assigned to the {target_biome} enclosure.")
            return

        for animal in found:
            print(f"* {animal.name} the {animal.species} says: {animal.speak()}")

go = ZooManager()
test = input("Would you like to add another animal? (Y/N) ")
if test == "Y":





#TODO think of Extra functionality to add to project

#TODO Check overall encapsulation