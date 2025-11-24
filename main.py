'''
File: Main.py
Description: This module contains the running functionality of the program importing the relevant information.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random

import Animal
import Enclosure
import Staff
from Staff import Veterinarian, Zookeeper, Admin

all_animals = []
all_staff = []
all_enclosures = []

print('Welcome to Zootopia\'s very own Zoo management tool')


def main():
    go = ZooManager()
    starting_selection = input('What Zoo would you like to create? '
                               '\n1.Default'
                               '\n2.Randomised '
                               '\n3.Custom\n')

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


class ZooManager:
    '''Contains the overall function of the Zoo Manager, holding the ability to drive and select from menus'''
    day_index = 0

    def __init__(self):
        self.all_animals = []
        self.all_staff = []
        self.all_enclosures = []
        self.new_animals = []
        self.new_staff = []
        self.new_enclosures = []
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
                            '\n3. List by Biome'
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
        '''This is used to create the objects for the Default Zoo settings.'''
        print('--- Generating Default Zoo ---')

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

        # 4. Add animals to the correct biome
        print('...Assigning animals to enclosures...')
        savannah.add_animal(simba)
        arctic.add_animal(pingu)
        jungle.add_animal(mei)
        water.add_animal(barry)
        brush.add_animal(bingo)

        # 5. Update the Manager's Master Lists
        self.all_enclosures.extend(new_enclosures)
        self.all_staff.extend(new_staff)
        self.all_animals.extend(new_animals)

        print(f'Done!'
              f'\n{len(new_enclosures)} Enclosures constructed.'
              f'\n{len(new_animals)} Animals added.'
              f'\n{len(new_staff)} Staff hired.')

    def get_random_zoo(self):
        print('--- Generating Random Zoo ---')

        # 1. Random Enclosures
        for i in range(5):
            random_biome = random.choice(Enclosure.Enclosure.biomes)

            enc = Enclosure.Enclosure(f'Habitat {i + 1}', random_biome, area=random.randint(500, 2000))
            self.all_enclosures.append(enc)

        # 2. Random Animals
        for enc in self.all_enclosures:
            if random.random() > 0.5:
                pass

                # 3. Random Staff
        # ... similar logic ...

        print('Random Zoo Created!')

    def menu_main(self):
        '''Holds the main menu for driving down to sub-menus'''
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
                self.day_summary()
                self.day_increment()
                return
            elif menu_choice == '9':
                print('Exiting Zoo Manager, see you next time :)')
                self.open_zoo = False

    def menu_staff(self):
        '''Holds the main staff menu for selecting sub-menus'''
        print()
        print(self.staff_menu)
        staff_menu_input = input('Which Staff menu would you like to explore? ')

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
        jobs = {}
        for staff in self.all_staff:
            if staff.function not in jobs:
                jobs[staff.function] = []
            jobs[staff.function].append(staff.name)

        print('\n--- Staff by Job Role ---')
        for job, names in jobs.items():
            print(f'**{job}** ({len(names)}): {', '.join(names)}')

    # TODO staff can only perform a number of actions, then you will need more staff or things will get dirty
    def menu_staff_actions(self):
        '''clean, feed, heal'''
        for staff in self.all_staff:
            print(f'* {staff.name} is a(n) {staff.function}')
        staff_selection = input('Which staff would you like to command? ')
        for staff in self.all_staff:
            if staff.name == staff_selection:
                print('What you have them do')
                if staff.function == Veterinarian:
                    #heal# Veterinarian = heal
                    pass
                elif staff.function == Zookeeper:
                    #clean or feed#Zookeeper = clean and feed
                    pass
                elif staff.function == Admin:
                    print('Don\'t be silly, admin\'s dont do anything')
            else:
                print('There is no staff with that name')
        pass

    def menu_staff_add(self):
        '''new staff, random choice name, append all staff'''
        print('--- New Staff ---')
        staff_type = input('Select Staff Type: '
                           '\n1. Zookeeper'
                           '\n2. Veterinarian'
                           '\n3. Admin'
                           '\nSelection: ')

        if staff_type in ('1', '2', '3'):
            name = input('Enter Staff Name (Leave blank for random): ')

            new_staff = None
            if staff_type == '1':
                new_staff = Staff.Zookeeper(name if name else None)
            elif staff_type == '2':
                new_staff = Staff.Veterinarian(name if name else None)
            elif staff_type == '3':
                new_staff = Staff.Admin(name if name else None)

            self.all_staff.append(new_staff)
            self.new_staff.append(new_staff)

            print(f'Successfully hired {new_staff.name} as a {new_staff.function}.')
        else:
            print('Invalid staff type selection.')

    def menu_staff_remove(self):
        '''remove staff from list'''
        print('\n--- Staff Termination Menu ---')
        self.menu_staff_list_all()

        staff_to_remove_name = input('Enter the name of the staff member to remove: ').capitalize()
        staff_object_to_remove = None

        for staff in self.all_staff:
            if staff.name == staff_to_remove_name:
                staff_object_to_remove = staff
                break

        if staff_object_to_remove:
            self.all_staff.remove(staff_object_to_remove)
            print(f'{staff_object_to_remove.name} ({staff_object_to_remove.function}) has been let go.')
        else:
            print(f'Staff member {staff_to_remove_name} not found.')

    def menu_enclosures(self):
        '''Holds the main Enclosure menu for selecting sub-menus'''
        print()
        print(self.enclosure_menu)

        staff_menu_input = input('Which Enclosures menu would you like to explore? ')
        if staff_menu_input == '1':
            self.menu_enclosures_list_all()
            return
        elif staff_menu_input == '2':
            self.menu_enclosures_by_biome()
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

    def menu_increase_enclosure_size(self):
        for enclosure in self.all_enclosures:
            print(f'* {enclosure.name}')
        enclosure_increase = input('Which enclosure wou you like to expand?').title()
        for enclosure in self.all_enclosures:
            if enclosure_increase == enclosure.name:
                new_size = input('Enter the new enclosure size: ')
                enclosure.area = new_size

    def menu_enclosures_list_all(self):
        if not self.all_enclosures:
            print('No enclosures have been built yet.')
            return

        print('\n--- All Enclosures ---')
        for index, enclosure in enumerate(self.all_enclosures):
            occupants = enclosure.get_occupants()
            print(f'{index + 1}. {enclosure.name} ({enclosure.biome}, {enclosure.area}m²) - Occupants: {occupants}')

    def menu_enclosures_by_biome(self):
        pass

    def menu_enclosures_by_cleanliness(self):
        enclosure_by_cleanliness = sorted(self.all_enclosures,
                                          key=lambda enclosure: enclosure.cleanliness)
        print('Enclosures by cleanliness:')
        for index, enclosure in enumerate(enclosure_by_cleanliness):
            print(f'{index + 1}. {enclosure.name} | Cleanliness: {enclosure.cleanliness}')

    def menu_enclosure_add(self):
        name = input('Enter Enclosure Name: ').title()
        #TODO requires name to be entered
        if name in self.all_enclosures:
            print('Enclosure already exists.')
            return
        print(f'Available Biomes: {Enclosure.Enclosure.biomes}')
        biome = input('Enter Biome: ')

        try:
            area = float(input('Enter Area (m²): '))
        except ValueError:
            print('Invalid area input. Aborting.')
            return

        new_enclosure = Enclosure.Enclosure(name, biome, area)
        new_enclosure.new_enclosure()

        self.all_enclosures.append(new_enclosure)
        self.new_enclosures.append(new_enclosure)

        print(f'Successfully added {new_enclosure.name}!')

    def menu_enclosure_remove(self):
        print('Enclosure Closure')
        for enclosure in self.all_enclosures:
            print(f'{enclosure.name}')

        enclosure_to_remove = input('Which Enclosure do you want to close? ').title()
        enclosure_object_to_remove = None
        for enclosure in self.all_enclosures:
            if enclosure.name == enclosure_to_remove:
                enclosure_object_to_remove = enclosure
        if enclosure_object_to_remove:
            self.all_enclosures.remove(enclosure_object_to_remove)
            print(f'Successfully removed {enclosure_object_to_remove.name}')
        else:
            print(f'Enclosure {enclosure_to_remove} not found.')

    def menu_animals(self):
        '''Holds the main Animal menu for selecting sub-menus'''
        print()
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
        print(f'All animals in the Zoo:')
        for animal in self.all_animals:
            print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')

    def set_animals_by_diet(self):
        meat_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Meat':
                meat_diet.append(animal.name)
        plant_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Plants':
                plant_diet.append(animal.name)

    def menu_animals_by_diet(self):
        diet_choice = input('Would you like to see:'
                            '\n1. Carnivores'
                            '\n2. Herbivores'
                            '\nSelection: ')
        if diet_choice == '1':
            for animal in self.all_animals:
                if animal.diet == 'Meat':
                    print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')
        elif diet_choice == '2':
            for animal in self.all_animals:
                if animal.diet == 'Plants':
                    print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')
        else:
            print('Invalid choice.')

    def menu_animals_by_biome(self):
        for enclosure in self.all_enclosures:
            print(f'* {enclosure.name} | Biome: {enclosure.biome}')
        target_biome = input('Which biome\'s inhabitants do you want to check? ').capitalize()

        print(f'\n--- Animals in the {target_biome} Enclosure ---')
        found = [animal for animal in self.all_animals if animal.biome == target_biome]

        if not found:
            print(f'No animals currently assigned to the {target_biome} enclosure.')
            return

        for animal in found:
            print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')

    def menu_animals_health_card(self):
        print('\n--- Animal Health Card Selection ---')

        for animal in self.all_animals:
            print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')

        animal_selection_id = input('Enter the ID of the animal (e.g., A001): ').upper()

        for animal in self.all_animals:
            if animal_selection_id == animal.animal_id:
                animal.health_record()
                return

        print(f'Invalid Selection: Animal ID {animal_selection_id} not found.')

    def menu_animals_add(self):
        print('\n--- Acquire New Animal ---')
        available_species = Animal.Animal.get_all_concrete_animal_types()
        print(f'Available Species: {', '.join(available_species)}')

        species_choice = input('Enter the Species name: ')
        name = input('Enter the Animal\'s Name (Leave blank for random): ')
        #TODO add animal age when adding to the zoo
        try:
            animal_class = getattr(Animal, species_choice)
            new_animal = animal_class(name if name else None)

        except (AttributeError, TypeError):
            print(f'Invalid species: {species_choice} or creation error.')
            return

        suitable_enclosure = None
        for enclosure in self.all_enclosures:
            if enclosure.add_animal(new_animal):
                suitable_enclosure = enclosure

        if suitable_enclosure:
            self.all_animals.append(new_animal)
            self.new_animals.append(new_animal)
            print(
                f'New arrival! {new_animal.name} the {new_animal.species} is settling into {suitable_enclosure.name}.')
        else:
            print(f'Unable to home {new_animal.name}. No suitable enclosure found.'
                  f'\nAdd a new enclosure for this animal first')

    # TODO Remove by ID, for animals of same name
    def menu_animals_remove(self):
        '''Attempts to remove an animal, running all checks.'''
        print('\n--- Animal Release Menu ---')

        for animal in self.all_animals:
            print(f'*{animal.name} the {animal.species}')

        animal_to_remove_name = input('Which animal are we releasing from captivity? ').capitalize()
        animal_object_to_release = None

        for animal in self.all_animals:
            if animal.name == animal_to_remove_name:
                animal_object_to_release = animal

        if animal_object_to_release:
            self.all_animals.remove(animal_object_to_release)
            for enclosure in self.all_enclosures:
                if animal_object_to_release in enclosure.animals:
                    enclosure.animals.remove(animal_object_to_release)
                    print(f'Removed {animal_object_to_release.name} from {enclosure.name}.')
            print(f'{animal_to_remove_name} was sent back to the wild! Goodbye...')
        else:
            print(f'Invalid Selection: Animal {animal_to_remove_name} not found.')

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

        print('*----------------------------------*'
              '\nSummary of the day:')

        if self.new_animals:
            print()
            print('New Animals Added:')
            for animal in self.new_animals:
                print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')
            self.new_animals = []
        else:
            print('No new animals were added today')

        if self.new_enclosures:
            print()
            print('New Enclosures Added:')
            for enclosure in self.new_enclosures:
                print(f'{enclosure.name} ({enclosure.biome}, {enclosure.area}m²')
            self.new_enclosures = []
        else:
            print('No new enclosures were added today')

        if self.new_staff:
            print()
            print('New Staff Added:')
            for staff in self.new_staff:
                print(f'* {staff.name} is a(n) {staff.function}')
            self.new_staff = []
        else:
            print('No new staff were added today')
        print('*----------------------------------*')
    def is_open(self):
        while self.open_zoo:
            print()
            self.menu_main()

    # TODO implement way of incrementing days with actions required.

    # TODO think of Extra functionality to add to project

    # TODO Check overall encapsulation


if __name__ == '__main__':
    main()
