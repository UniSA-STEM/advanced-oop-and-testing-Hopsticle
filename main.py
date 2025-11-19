'''
File: Main.py
Description: This module contains the different staff roles and the individuals information
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random
import Enclosure
import Animal
import Staff
import Utilities

all_animals = Animal.all_animals
all_staff = Staff.all_staff
all_enclosures = Enclosure.all_enclosures

print('Welcome to Zootopia\'s very own Zoo management tool')


def main():
    go = ZooManager()
    starting_selection = input('What Zoo would you like to create? '
                               '\n1.Default'
                               '\n2.Randomised '
                               '\n3.Custom\n')
    # TODO setter in main then getter in Zoo manager
    if starting_selection == '1':
        go.get_default()

    elif starting_selection == '2':
        '''add 5 random enclosures with compatible animal, and one of each staff'''
        # Utilities.generate_random_zoo(go)
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
    go.is_open()


# TODO implement main and zoom manager functions
class ZooManager:
    '''Contains the overall function of the Zoo Manager, holding the ability to drive and select from menus'''
    day_index = 0

    def __init__(self):
        self.all_animals = []
        self.all_staff = []
        self.all_enclosures = []
        self.open_zoo = True

        self.menu_items = ('---Main Menu---'
                           '\n1. Animals'
                           '\n2. Staff'
                           '\n3. Enclosures'
                           '\n4. End Day'
                           '\n9. Exit')

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

    def get_default(self):
        print('--- Generating Default Zoo State ---')

        # 1. Construct Enclosures
        savannah = Enclosure.Enclosure('Pride Rock', 'Savannah', 200)
        arctic = Enclosure.Enclosure('Ice Caps', 'Arctic', 50)
        jungle = Enclosure.Enclosure('Bamboo Grove', 'Jungle', 80)
        water = Enclosure.Enclosure('Blue Lagoon', 'Water', 100)
        brush = Enclosure.Enclosure('Outback', 'Brush', 150)

        new_enclosures = [savannah, arctic, jungle, water, brush]

        # 2. Hire Staff
        jesse = Staff.Zookeeper('Jesse')
        james = Staff.Veterinarian('James')
        ash = Staff.Admin('Ash')

        new_staff = [jesse, james, ash]

        # 3. Acquire Animals
        simba = Animal.Lion('Simba')  # Needs Savannah
        pingu = Animal.Penguin('Pingu')  # Needs Arctic
        mei = Animal.RedPanda('Mei')  # Needs Jungle
        barry = Animal.Barracuda('Barry')  # Needs Water
        bingo = Animal.Dingo('Bingo')  # Needs Brush

        new_animals = [simba, pingu, mei, barry, bingo]

        print('...Assigning animals to habitats...')
        savannah.add_animal(simba)
        arctic.add_animal(pingu)
        jungle.add_animal(mei)
        water.add_animal(barry)
        brush.add_animal(bingo)

        # 5. Update the Manager's Master Lists
        self.all_enclosures.extend(new_enclosures)
        self.all_staff.extend(new_staff)
        self.all_animals.extend(new_animals)

        print(f'Done! \n{len(new_animals)} Animals added.'
              f'\n{len(new_staff)} Staff hired.'
              f'\n{len(new_enclosures)} Enclosures constructed.')

    def get_random_zoo(self):
        print('--- Generating Random Zoo State ---')

        # 1. Random Enclosures
        for i in range(5):
            random_biome = random.choice(Enclosure.Enclosure.biomes)

            enc = Enclosure.Enclosure(f"Habitat {i + 1}", random_biome, area=random.randint(500, 2000))
            self.all_enclosures.append(enc)

        # 2. Random Animals
        for enc in self.all_enclosures:
            if random.random() > 0.5:
                pass

                # 3. Random Staff
        # ... similar logic ...

        print("Random Zoo Created!")

    def menu_main(self):
        while self.open_zoo:
            print(self.menu_items)
            menu_choice = input('Which menu would you like to explore? ')

            if menu_choice == '1':
                self.menu_animals()
                return
            elif menu_choice == '2':
                self.menu_staff()
                return
            elif menu_choice == '3':
                self.menu_enclosures()
                return
            elif menu_choice == '4':
                self.day_increment()
                return
            elif menu_choice == '9':
                print('The zoo has been closed.')

    def menu_staff(self):
        print()
        print(self.staff_menu)
        staff_menu_input = input('Which menu would you like to explore? ')

        if staff_menu_input == '1':
            self.menu_staff_list_all()
            return
        elif staff_menu_input == '2':
            self.menu_staff_by_job()
            return
        elif staff_menu_input == '3':
            self.menu_staff_actions()
            return
        elif staff_menu_input == '4':
            self.menu_staff_add()
            return
        elif staff_menu_input == '5':
            self.menu_staff_remove()
            return

    def menu_staff_list_all(self):
        for staff in self.all_staff:
            print(f'* {staff.name} is a(n) {staff.function}')

    def menu_staff_by_job(self):
        # for staff in
        pass

    # TODO staff can only perform a number of actions, then you will need more staff or things will get dirty
    def menu_staff_actions(self):
        '''clean, feed, heal'''
        pass

    def menu_staff_add(self):
        '''new staff, random choice name, append all staff'''
        # TODO add staff takes three days. add volunteers immediately? volunteers at all?
        pass

    def menu_staff_remove(self):
        '''remove staff from list'''
        pass

    def menu_enclosures(self):
        print(self.enclosure_menu)

        staff_menu_input = input('Which menu would you like to explore? ')
        if staff_menu_input == '1':
            self.menu_enclosures_list_all()
            return
        elif staff_menu_input == '2':

            return
        elif staff_menu_input == '3':
            self.menu_enclosures_by_cleanliness()
            return
        elif staff_menu_input == '4':
            self.menu_enclosure_add()
            return
        elif staff_menu_input == '5':
            self.menu_enclosure_remove()
            return

    def menu_enclosures_list_all(self):
        if not self.all_enclosures:
            print('No enclosures have been built yet.')
            return

        print('\n--- All Enclosures ---')
        for index, enclosure in enumerate(self.all_enclosures):
            occupants = enclosure.get_occupants()
            print(f'{index + 1}. {enclosure.name} ({enclosure.biome}, {enclosure.area}m²) - Occupants: {occupants}')

    def menu_enclosures_by_cleanliness(self):
        sorted_by_cleanliness = sorted(self.all_enclosures, key=lambda enclosure: enclosure.cleanliness)
        print(sorted_by_cleanliness)

    def list_by_cleanliness(self):
        enclosure_by_cleanliness = sorted(all_enclosures,
                                          key=lambda enclosure: enclosure.cleanliness)
        print('Enclosures by cleanliness:')
        for index, enclosure in enumerate(enclosure_by_cleanliness):
            print(f'{index + 1}. {enclosure.name} | Cleanliness: {enclosure.cleanliness}')

    def menu_enclosure_add(self):
        name = input('Enter Enclosure Name: ')
        print(f'Available Biomes: {Enclosure.Enclosure.biomes}')
        biome = input('Enter Biome: ')

        try:
            area = float(input('Enter Area (m²): '))
        except ValueError:
            print('Invalid area input. Aborting.')
            return

        new_enclosure = Enclosure.Enclosure(name, biome, area)
        new_enclosure.new_enclosure()

        print(f'Successfully added {name}!')

    def menu_enclosure_remove(self):
        print(f'{all_enclosures}')
        enclosure_to_remove = input('Which Enclosure do you want to close?').capitalize()
        for enclosure in self.all_enclosures:
            if enclosure.name == enclosure_to_remove:
                all_enclosures.remove(enclosure_to_remove)
            print(f'Successfully removed {enclosure_to_remove}')

    def menu_animals(self):
        print(self.animal_menu)
        animals_menu_input = input('Which Animals menu would you like to explore? ')

        if animals_menu_input == '1':
            self.menu_animals_list_all()
            return
        elif animals_menu_input == '2':
            self.menu_animals_by_diet()
            return
        elif animals_menu_input == '3':
            self.menu_animals_by_biome()
            return
        elif animals_menu_input == '4':
            self.menu_animals_health_card()
            return
        elif animals_menu_input == '5':
            self.menu_animals_add()
            return
        elif animals_menu_input == '6':
            self.menu_animals_remove()
            return


    def menu_animals_list_all(self):
        print(f'Animals in no order:')
        for animal in self.all_animals:
                  print(f'* {animal.name}')

    def set_animals_by_diet(self):
        meat_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Meat':
                meat_diet.append(animal.name)
        plant_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Plant':
                plant_diet.append(animal.name)

    def menu_animals_by_diet(self):
        diet_choice = input('Would you like to see:'
                            '\n1. Carnivores'
                            '\n2. Herbivores')
        if diet_choice == '1':
            for animal in self.meat_diet:
                print(f'*\n{animal.name}')
        elif diet_choice == '2':
            for animal in self.plant_diet:
                print(f'*\n{animal.name}')
        else:
            print('Invalid choice.')

    def menu_animals_by_biome(self, target_biome):
        print(f'\n--- Animals in the {target_biome} Enclosure ---')
        found = [animal for animal in self.all_animals if animal.biome == target_biome]

        if not found:
            print(f'No animals currently assigned to the {target_biome} enclosure.')
            return

        for animal in found:
            print(f'* {animal.name} the {animal.species} says: {animal.speak()}')

    def list_animals_by_biome(self, target_biome):
        target_biome = input('For which biome would you like the check on the animals of?')

        print(f'\n--- Animals in the {target_biome} Enclosure ---')
        found = [animal for animal in self.all_animals if animal.biome == target_biome]

        if not found:
            print(f'No animals currently assigned to the {target_biome} enclosure.')
            return

        for animal in found:
            print(f'* {animal.name}')

    def menu_animals_health_card(self):
        # 1. Access the instance list
        self.menu_animals_list_all()

        animal_selection = input('Which animal would you like to see? ').capitalize()
        found = False

        # 2. Iterate through the manager's master list
        for animal in self.all_animals:
            if animal_selection == animal.name:
                # 3. Call the method on the specific animal OBJECT
                animal.health_record()
                found = True
                return

        if not found:
            print(f"Invalid Selection: Animal '{animal_selection}' not found in the zoo.")

    def menu_animals_add(self, animal_object):
        '''Attempts to add an animal, running all checks.'''
        if animal_object.biome != self.biome:
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

    def menu_animals_remove(self):
        for animal in self.all_animals:
            print(f'*{animal.name} the {animal.species}')
        animal_to_remove = input('Enter Animal Name: ').capitalize()
        for animal in all_animals:
            if animal is animal_to_remove:
                all_animals.remove(animal_to_remove)
                print(f'{animal_to_remove} was sent back to the wild! Goodbye...')

    # TODO if an animal gets sick 80% chance another in the enclosure also gets sick if not tended to.. sick for too long die...?
    def sick_animal(self):
        sickness_spread = False
        sick_animals = []
        for animal in self.all_animals:
            sick_animals.append(animal.name)
            if animal.health == 0:
                sickness_spread = True

        if sickness_spread:
            pass

        if not sickness_spread:
            sick_chance = random.randint(0, 100)
            if sick_chance > 95:
                random_animal = random.choice(list(self.all_animals))
                random_animal.health = 0
                print(f'{random_animal.name} is sick and needs to see a Vet')
            else:
                print('No animals became unhealthy overnight.. Phew!!')

    def day_increment(self):
        self.day_index += 1
        self.sick_animal()
        for animal in self.all_enclosures:
            animal.cleanliness -= 5

    # TODO with each new day list changes if any, from overnight
    def day_summary(self):

        print('Summary of the day:')
        if self.new_animals:
            print('New Animals Added:')
            for animal in self.new_animals:
                print(f'\n{animal.name}')
                self.new_animals = []
                Animal.Animal.set_animals_by_diet(animal.diet)
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

    def is_open(self):
        while self.open_zoo:
            print()
            self.menu_main()

    # TODO implement way of incrementing days with actions required.

    # TODO think of Extra functionality to add to project

    # TODO Check overall encapsulation


if __name__ == '__main__':
    main()
