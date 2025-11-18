'''
File: Main.py
Description: This module contains the different staff roles and the individuals information
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random
from linecache import clearcache

import Staff
import Enclosure
import Animal

all_animals = Animal.all_animals
all_staff = Staff.all_staff
all_enclosures = Enclosure.all_enclosures

print('Welcome to Zootopia\'s very own Zoo management tool')

def main():
    pass
    starting_selection = input('What Zoo would you like to create? '
          '\n1.Default'
          '\n2.Randomised '
          '\n3.Custom\n')
    #TODO setter in main then getter in Zoo manager
    if starting_selection == '1':
        ZooManager.get_default()

    elif starting_selection == '2':
        '''add 5 random enclosures with compatible animal, and one of each staff'''
        pass
    else:
        animal_choice = input('How many animals would you like? ')
        for animal in animal_choice:
            '''add random animals plus respective biomes/enclosures'''
            pass
        staff_choice = input('How many staff would you like? ')
        for staff in staff_choice:
            '''add random staff'''
            pass

    zoo_manager = ZooManager(all_animals, all_staff, all_enclosures)
    zoo_manager.start_day()


#TODO implement main and zoom manager functions
class ZooManager:
    day_index = 0
    def __init__(self):
        self.all_animals = Animal.all_animals
        self.all_staff = Staff.all_staff
        self.all_enclosures = Enclosure.all_enclosures
        self.new_animals = []
        self.new_enclosures = []
        self.new_staff = []
        self.cleanliness = Enclosure.Enclosure.get_cleanliness

        self.menu_items = ('---Main Menu---'
                           '\n1. Animals'
                           '\n2. Staff'
                           '\n3. Enclosures')

        self.animal_menu = ('---Animals---'
                            '\n1. List All'
                            '\n2. List by Diet'
                            '\n3. List by '
                            '\n4. Animal Health Card'
                            '\n5. Add Animal'
                            '\n6. Remove Animal')

        self.staff_menu = ('---Staff---'
                           '\n1. List All'
                           '\n2. List by Job'
                           '\n3. Staff Actions'
                           '\n4. Add Staff'
                           '\n5. Remove Staff')

        self.enclosure_menu = ('---Enclosure---'
                               '\n1. List All'
                               '\n2. List by Biome'
                               '\n3. List by Cleanliness'
                               '\n4. Add Enclosure'
                               '\n5. Remove Enclosure')

    def set_default(self):
        self.all_animals = []
        '''lion, penguin, red panda, barracuda, dingo'''
        self.all_staff = []
        '''Jesse, James, Ash'''
        self.all_enclosures = []
        '''savannah, arctic, jungle, water, brush'''

    def get_default(self):
        self.set_default()
        pass

    def menu_main(self):
        print(self.menu_items)

    def menu_staff(self):
        print(self.staff_menu)

    def menu_list_all_staff(self):
        for staff in self.all_staff:
            print(f'{staff.name} is a {staff.function}')

    def menu_list_by_job(self):
        # for staff in
        pass

    def menu_staff_actions(self):
        '''clean, feed, heal'''
        pass

    def menu_add_staff(self):
        '''new staff, random choice name, append all staff'''
        #TODO add staff takes three days. add volunteers immediately?
        pass

    def menu_remove_staff(self):
        '''remove staff from list'''
        pass

    def menu_list_all_enclosures(self):
        if not self.all_enclosures:
            print('No enclosures have been built yet.')
            return

        print('\n--- All Enclosures ---')
        for i, enclosure in enumerate(self.all_enclosures):
            occupants = enclosure.get_occupants()
            print(f'{i + 1}. {enclosure.name} ({enclosure.biome}, {enclosure.area}m²) - Occupants: {occupants}')

    def menu_list_by_cleanliness(self):
        sorted_by_cleanliness =sorted(self.all_enclosures, key=lambda enclosure: enclosure.cleanliness)
        print(sorted_by_cleanliness)


    def menu_add_enclosure(self):
            name = input('Enter Enclosure Name: ')
            print(f'Available Biomes: {Enclosure.biomes}')
            biome = input('Enter Biome: ')

            try:
                area = float(input('Enter Area (m²): '))
            except ValueError:
                print('Invalid area input. Aborting.')
                return

            new_enclosure = Enclosure.Enclosure(name, biome, area)
            new_enclosure.new_enclosure()

            print(f'Successfully added {name}!')

    def menu_remove_enclosure(self):
        print(f'{all_enclosures}')
        enclosure_to_remove = input('Which Enclosure do you want to close?').capitalize()
        self.all_enclosures.remove(enclosure_to_remove)
        print(f'Successfully removed {enclosure_to_remove}')

    def menu_animals(self):
        return self.animal_menu

    def menu_list_all_animals(self):
        for animal in self.all_animals:
            print(f'Animals in no order:'
                  f'\n*{animal.name}')

    def menu_list_all_by_diet(self):
        meat_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Meat':
                meat_diet.append(animal.diet)
        plant_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Plant':
                plant_diet.append(animal.diet)
        diet_choice = input('Would you like to see:'
                            '\n1. Carnivores'
                            '\n2. Herbivores')
        if diet_choice == '1':
            print(f'\n{meat_diet}')
        else:
            print(f'\n{plant_diet}')

    def menu_health_card_menu(self):
        pass

    def menu_add_animal(self, animal_object):
        '''Attempts to add an animal, running all checks.'''
        if animal_object.biome != Enclosure.biome:
            print(
                f'Couldn\'t add {animal_object.name}: Wrong Biome. Needs {animal_object.biome}, found {self.biome}.')
            return
        # TODO when adding new animal ensure there is an enclosure ready to move into with enough space
        if not Enclosure.Enclosure.check_size(animal_object):
            print(
                f'Failed to add {animal_object.name}: Not enough space (Required {animal_object.get_min_enclosure_area()}m²).')
            return
        # TODO Takes a day for animal to arrive,
        if not Enclosure.Enclosure.check_safety(animal_object):
            return

    def menu_remove_animal(self):
        for animal in self.all_animals:
            print(f'*{animal.name} the {animal.species}')
        animal_to_remove = input('Enter Animal Name: ').capitalize()
        self.all_animals.remove(animal_to_remove)
        print(f'{animal_to_remove} was sent back to the wild!')



    def enclosure_menu(self):
        print(self.enclosure_menu)

    def list_animals_by_biome(self, target_biome):
        target_biome = input('For which biome would you like the check on the animals of?')

        print(f'\n--- Animals in the {target_biome} Enclosure ---')
        found = [animal for animal in self.all_animals if animal.biome == target_biome]

        if not found:
            print(f'No animals currently assigned to the {target_biome} enclosure.')
            return

        for animal in found:
            print(f'* {animal.name}')

    def sick_animal(self):
        sick_chance = random.randint(0, 100)
        if sick_chance > 95:
            random_animal = random.choice(list(self.all_animals))
            random_animal.health = 0
            print(f'{random_animal.name} is sick and needs to see a Vet')
        else:
            print('No animals became unhealthy overnight.. Phew!!')

    def day_increment(self, cleanliness):
        self.day_index += 1
        self.sick_animal()
        for found in self.all_enclosures:
            self.cleanliness -= 5

    # TODO with each new day list changes if any, from overnight
    def day_summary(self):

        print('Summary of the day:')
        if self.new_animals:
            print('New Animals Added:')
            for animal in self.new_animals:
                print(f'\n{animal.name}')
                self.new_animals = []
        else:
            print('No new animals were added today')
        if self.new_enclosures:
            print('New Enclosures Added:')
            for new in self.new_enclosures:

                print(f'\n{new.name}')
                self.new_enclosures = []
        else:
            print('No new enclosures were added today')
        if self.new_staff:
            print('New Staff Added:')
            for new in self.new_staff:
                print(f'\n{new.name}')
                self.new_staff = []
        else:
            print('No new staff were added today')



    #TODO implement way of incrementing days with actions required.

    #TODO think of Extra functionality to add to project

    #TODO Check overall encapsulation

if __name__ == '__main__':
    main()