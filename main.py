'''
File: Main.py
Description: This module contains the running functionality of the program importing the relevant information.
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random

# Import necessary classes from other modules
import Animal
import Enclosure
import Staff
from Staff import Veterinarian, Zookeeper, Admin

# Global lists to hold all objects across the application
all_animals = []
all_staff = []
all_enclosures = []

print('Welcome to Zootopia\'s very own Zoo management tool')


def main():
    # Instantiate the ZooManager class
    go = ZooManager()

    # Prompt user for the initial setup of the zoo
    starting_selection = input('What Zoo would you like to create? '
                               '\n1.Default'
                               '\n2.Randomised '
                               '\n3.Custom'
                               '\nSelection: ')

    if starting_selection == '1':
        # Load predefined zoo setup
        go.get_default()

    elif starting_selection == '2':
        # Generate a zoo with random enclosures, staff, and animals
        go.get_random_zoo()
    else:
        # Custom setup is handled by the main loop (currently not implemented in a custom way)
        pass

    # Start the main loop/zoo operation
    go.is_open()


class ZooManager:
    '''Contains the overall function of the Zoo Manager, holding the ability to drive and select from menus'''
    day_index = 0 # Class attribute, but instance attribute is also used

    def __init__(self):
        # References to the global master lists
        self._all_animals = all_animals
        self._all_staff = all_staff
        self._all_enclosures = all_enclosures

        # Lists for tracking newly added objects during the current day (for summary)
        self._new_animals = []
        self._new_staff = []
        self._new_enclosures = []

        # Internal state variables
        self._day_index = 0
        self._open_zoo = True

        # Menu options strings
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

    # Property methods to access the master lists (read-only access to protected attributes)
    @property
    def all_animals(self):
        return self._all_animals

    @property
    def all_staff(self):
        return self._all_staff

    @property
    def all_enclosures(self):
        return self._all_enclosures

    @property
    def day_index(self):
        return self._day_index

    @property
    def open_zoo(self):
        return self._open_zoo

    def day_increment(self):
        '''Increments the day count and applies daily changes (sickness, enclosure dirtiness).'''
        self._day_index += 1
        self.sick_animal() # Check for new sickness

        # Enclosures get dirtier each day
        for enclosure in self._all_enclosures:
            enclosure.cleanliness -= 5

    def day_summary(self):
        '''This is used to output a summary of the changes that occurred during the day'''
        print('*----------------------------------*')
        print('Summary of the day:')

        # Report on new animals added
        if self._new_animals:
            print()
            print('New Animals Added:')
            for animal in self._new_animals:
                print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')
            self._new_animals = [] # Clear the list for the next day
        else:
            print('No new animals were added today')

        # Report on new enclosures built
        if self._new_enclosures:
            print()
            print('New Enclosures Added:')
            for enclosure in self._new_enclosures:
                print(f'{enclosure.name} ({enclosure.biome}, {enclosure.area}m²')
            self._new_enclosures = [] # Clear the list for the next day
        else:
            print('No new enclosures were added today')

        # Report on new staff hired
        if self._new_staff:
            print()
            print('New Staff Added:')
            for staff in self._new_staff:
                print(f'* {staff.name} is a(n) {staff.function}')
            self._new_staff = [] # Clear the list for the next day
        else:
            print('No new staff were added today')
        print('*----------------------------------*')

    def is_open(self):
        '''The main loop for the zoo management tool.'''
        while self._open_zoo:
            print()
            self.menu_main()

    def get_default(self):
        '''This is used to create the objects for the Default Zoo settings.'''
        print('--- Generating Default Zoo ---')

        # Construct Enclosures with predefined names, biomes, and areas
        savannah = Enclosure.Enclosure('Pride Rock', 'Savannah', 200)
        arctic = Enclosure.Enclosure('Ice Caps', 'Arctic', 50)
        jungle = Enclosure.Enclosure('Bamboo Grove', 'Jungle', 80)
        water = Enclosure.Enclosure('Blue Lagoon', 'Water', 100)
        brush = Enclosure.Enclosure('Outback', 'Brush', 150)

        new_enclosures = [savannah, arctic, jungle, water, brush]

        # Hire Staff (Zookeeper, Veterinarian, Admin)
        jesse = Staff.Zookeeper('Jesse')
        james = Staff.Veterinarian('James')
        ash = Staff.Admin('Ash')

        new_staff = [jesse, james, ash]

        # Acquire Animals (specific species for the biomes)
        simba = Animal.Lion('Simba')
        pingu = Animal.Penguin('Pingu')
        mei = Animal.RedPanda('Mei')
        barry = Animal.Barracuda('Barry')
        bingo = Animal.Dingo('Bingo')
        new_animals = [simba, pingu, mei, barry, bingo]

        # Add animals to the correct/compatible enclosures
        print('...Assigning animals to enclosures...')
        savannah.add_animal(simba)
        arctic.add_animal(pingu)
        jungle.add_animal(mei)
        water.add_animal(barry)
        brush.add_animal(bingo)

        # Update the Manager's Master Lists
        self.all_enclosures.extend(new_enclosures)
        self.all_staff.extend(new_staff)
        self.all_animals.extend(new_animals)

        print(f'Done!'
              f'\n{len(new_enclosures)} Enclosures constructed.'
              f'\n{len(new_animals)} Animals added.'
              f'\n{len(new_staff)} Staff hired.')

    def get_random_zoo(self):
        '''add 5 random enclosures with compatible animal, and one of each staff'''
        print('\n--- Generating Random Zoo (5 Enclosures, 3 Staff, Random Animals) ---')

        # Hire 3 staff one of each role
        new_staff_members = [Zookeeper(), Veterinarian(), Admin()]
        for staff in new_staff_members:
            self.all_staff.append(staff)
            print(f'Hired {staff.name} as a {staff.function}.')

        # Randomise 5 biomes from the available list
        possible_biomes = Enclosure.Enclosure.biomes
        random.shuffle(possible_biomes)
        biomes_to_use = possible_biomes[:5]

        # Random Enclosure names from a pool
        enclosure_name_pool = ['Eunoia', 'Zephyr', 'Halcyon', 'Kalon', 'Elysian', 'Terra', 'Aether']
        random.shuffle(enclosure_name_pool)

        # Setup 5 enclosures with random names and sizes
        for index, biome in enumerate(biomes_to_use):
            name = f'{biome} {enclosure_name_pool[index]} Habitat'
            area = random.randint(50, 200) # Random area between 50 and 200
            new_enclosure = Enclosure.Enclosure(name, biome, area)
            self.all_enclosures.append(new_enclosure)
            print(f'\nBuilt Enclosure: {new_enclosure.name} ({new_enclosure.biome}, {new_enclosure.area}m²)')

        # Get all concrete animal species names
        all_species_names = Animal.Animal.get_all_concrete_animal_types()

        # Iterate through the newly created enclosures and try to add random animals
        for enclosure in self.all_enclosures:
            animals_added_count = 0
            num_animals_to_add = random.randint(1, 3) # Try to add 1 to 3 animals per enclosure

            for number in range(num_animals_to_add):
                for attempt in range(5): # Give 5 attempts to find a compatible animal species
                    species_name = random.choice(all_species_names)
                    try:
                        # Dynamically get the class object from the Animal module
                        animal_class = getattr(Animal, species_name)
                        temp_animal = animal_class(name=None)

                        # Attempt to add the animal to the enclosure
                        success, number = enclosure.add_animal(temp_animal)
                        if success:
                            self.all_animals.append(temp_animal)
                            animals_added_count += 1
                            break # Move to the next animal slot if successful
                    except AttributeError:
                        continue # Try a different species name if the attribute lookup fails
            if animals_added_count > 0:
                print(f'    - Successfully added {animals_added_count} animal(s) to {enclosure.name}.')
            else:
                print(f'    - Failed to place any animals in {enclosure.name}.')

        print('\n--- Random Zoo Generation Complete! ---')

    def menu_main(self):
        '''Holds the main menu for driving down to sub-menus'''
        while self._open_zoo:
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
                # End the day, show summary, and increment day count
                self.day_summary()
                self.day_increment()
                return
            elif menu_choice == '9':
                # Exit the program
                print('Exiting Zoo Manager, see you next time :)')
                self._open_zoo = False

    def menu_staff(self):
        '''Holds the main staff menu for selecting sub-menus'''
        print()
        print(self.staff_menu)
        staff_menu_input = input('Which Staff menu would you like to explore? ')

        # Direct to specific staff sub-menus based on input
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
        '''Lists all staff and returns a dict mapping selection ID to staff object.'''
        if not self.all_staff:
            print('No staff members currently hired.')
            return None

        print('\n--- Available Staff ---')
        staff_dict = {}
        for i, staff in enumerate(self.all_staff):
            print(f'{i + 1}. {staff.name} ({staff.function})')
            staff_dict[str(i + 1)] = staff # Map index+1 (string) to staff object
        return staff_dict

    def menu_staff_by_job(self):
        '''Groups and lists staff members by their job role.'''
        jobs = {}
        # Populate the dictionary with job roles as keys and staff names as a list of values
        for staff in self.all_staff:
            if staff.function not in jobs:
                jobs[staff.function] = []
            jobs[staff.function].append(staff.name)

        print('\n--- Staff by Job Role ---')
        # Print the grouped results
        for job, names in jobs.items():
            print(f'**{job}** ({len(names)}): {',  '.join(names)}')

    def sick_animals_list(self):
        '''Returns a list of names of animals whose health is 0 or less.'''
        sick_animals = []
        for animal in self.all_animals:
            if animal.health <= 0:
                sick_animals.append(animal.name)
        return sick_animals

    def menu_staff_actions(self):
        '''Handles actions staff members can perform (Clean, Feed, Heal).'''
        print('\n--- Staff Actions Menu ---')

        # List all staff and get the staff member to act
        staff_map = self.menu_staff_list_all()
        if not staff_map:
            return

        staff_choice = input('Select staff member ID for action: ')
        selected_staff = staff_map.get(staff_choice)

        if not selected_staff:
            print('Invalid staff choice.')
            return

        # Zookeeper Actions
        if isinstance(selected_staff, Zookeeper):
            print(f'\n{selected_staff.name} is a Zookeeper. What action should they perform?')
            action_choice = input('1. Clean Enclosure'
                                  '\n2. Feed Animals'
                                  '\nSelect action: ')

            if action_choice == '1':
                # Cleaning: Target dirty enclosures
                target_map = self.list_dirty_enclosures()
                if not target_map: return

                target_choice = input('Select enclosure ID to clean: ')
                target_enclosure = target_map.get(target_choice)

                if target_enclosure:
                    result = selected_staff.clean_enclosure(target_enclosure)
                    print(result)
                else:
                    print('Invalid enclosure choice.')

            elif action_choice == '2':
                # Feeding: Target all enclosures
                target_map = self.list_all_enclosures()
                if not target_map: return

                target_choice = input('Select enclosure ID to feed: ')
                target_enclosure = target_map.get(target_choice)

                if target_enclosure:
                    result = selected_staff.feed_animals(target_enclosure)
                    print(result)
                else:
                    print('Invalid enclosure choice.')
            else:
                print('Invalid action choice.')

        # Veterinarian Actions
        elif isinstance(selected_staff, Veterinarian):
            print(f'\n{selected_staff.name} is a Veterinarian. What action should they perform?')

            # Healing: Target sick animals
            target_map = self.list_sick_animals()
            if not target_map: return

            target_choice = input('Select animal ID to heal: ')
            target_animal = target_map.get(target_choice)

            if target_animal:
                result = selected_staff.heal_animal(target_animal)
                print(result)
            else:
                print('Invalid animal ID choice.')

        # Admin Actions
        elif isinstance(selected_staff, Admin):
            print(
                f'\n{selected_staff.name} is an Admin. They handle hiring staff and building enclosures, which are accessed via the main menus.')

        else:
            print('Staff member selected is of an unknown type.')

    def menu_staff_add(self):
        '''new staff, random choice name, append all staff'''
        print('\n--- New Staff ---')
        staff_type = input('Select Staff Type: '
                           '\n1. Zookeeper'
                           '\n2. Veterinarian'
                           '\n3. Admin'
                           '\nSelection: ')

        if staff_type in ('1', '2', '3'):
            name = input('Enter Staff Name (Leave blank for random): ')

            new_staff = None
            # Instantiate the correct staff class with the provided or random name
            if staff_type == '1':
                new_staff = Staff.Zookeeper(name if name else None)
            elif staff_type == '2':
                new_staff = Staff.Veterinarian(name if name else None)
            elif staff_type == '3':
                new_staff = Staff.Admin(name if name else None)

            # Add to master list and tracking list
            self.all_staff.append(new_staff)
            self._new_staff.append(new_staff)

            print(f'Successfully hired {new_staff.name} as a(n) {new_staff.function}.')
        else:
            print('Invalid staff type selection.')

    def menu_staff_remove(self):
        '''remove staff from list'''
        print('\n--- Staff Termination Menu ---')
        staff_map = self.menu_staff_list_all() # List staff to help the user choose

        staff_to_remove_name = input('Enter the name of the staff member to remove: ').capitalize()
        staff_object_to_remove = None

        # Find the staff member object by name
        for staff in self.all_staff:
            if staff.name == staff_to_remove_name:
                staff_object_to_remove = staff
                break

        if staff_object_to_remove:
            self.all_staff.remove(staff_object_to_remove) # Remove from master list
            print(f'{staff_object_to_remove.name} ({staff_object_to_remove.function}) has been let go.')
        else:
            print(f'Staff member {staff_to_remove_name} not found.')

    def menu_enclosures(self):
        '''Holds the main Enclosure menu for selecting sub-menus'''
        print()
        print(self.enclosure_menu)

        staff_menu_input = input('Which Enclosures menu would you like to explore? ')

        # Direct to specific enclosure sub-menus based on input
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
        '''Allows the user to manually increase the area of an existing enclosure.'''
        for enclosure in self.all_enclosures:
            print(f'* {enclosure.name}')
        enclosure_increase = input('Which enclosure wou you like to expand?').title()

        # Find the enclosure and update its area
        for enclosure in self.all_enclosures:
            if enclosure_increase == enclosure.name:
                new_size = input('Enter the new enclosure size: ')
                enclosure.area = new_size # Directly set the new area

    def menu_enclosures_list_all(self):
        '''Lists all enclosures, their biome, size, and current occupants.'''
        print()
        if not self.all_enclosures:
            print('No enclosures have been built yet.')
            return

        print('\n--- All Enclosures ---')
        for index, enclosure in enumerate(self.all_enclosures):
            occupants = enclosure.get_occupants() # Get the names of animals in the enclosure
            print(f'{index + 1}. {enclosure.name} ({enclosure.biome}, {enclosure.area}m²) - Occupants: {occupants}')


    def list_all_enclosures(self):
        '''Lists all enclosures and returns a dict mapping selection ID to enclosure object.'''
        if not self.all_enclosures:
            print('No enclosures in the zoo.')
            return None

        print('\n--- All Enclosures ---')
        enclosure_dictionary = {}
        # List enclosures and count occupants
        for index, enclosure in enumerate(self.all_enclosures):
            occupants = f'({len(enclosure.animals)} animal{'s' if len(enclosure.animals) != 1 else ''})'
            print(f'{index + 1}. {enclosure.name} {occupants}')
            enclosure_dictionary[str(index + 1)] = enclosure
        return enclosure_dictionary

    def menu_enclosures_by_biome(self):
        '''Groups and lists enclosures based on their biome.'''
        print('\n--- Enclosures Listed by Biome ---')

        if not self.all_enclosures:
            print('No enclosures have been built yet.')
            return

        biomes_map = {}
        # Group enclosures by biome
        for enclosure in self.all_enclosures:
            if enclosure.biome not in biomes_map:
                biomes_map[enclosure.biome] = []
            biomes_map[enclosure.biome].append(enclosure)

        # Print the grouped results
        for biome in sorted(biomes_map.keys()):
            print(f'\n[ {biome.upper()} BIOME ({len(biomes_map[biome])} Enclosures) ]')

            for enclosure in biomes_map[biome]:
                occupants = enclosure.get_occupants()

                print(f'* {enclosure.name} ({enclosure.area}m²) - Cleanliness: {enclosure.cleanliness}%')
                print(f'  - Occupants: {occupants}')

    def list_dirty_enclosures(self, min_cleanliness=80):
        '''Lists enclosures below a cleanliness threshold and returns a dict mapping selection ID to enclosure object.'''
        print()
        # Filter for enclosures below the specified cleanliness
        dirty_enclosures = [enclosure for enclosure in self.all_enclosures if enclosure.cleanliness < min_cleanliness]
        if not dirty_enclosures:
            print('All enclosures are sparkling clean!')
            return None

        print(f'\n--- Enclosures Needing Cleaning (Cleanliness < {min_cleanliness}) ---')
        enclosure_dictionary = {}
        for index, enclosure in enumerate(dirty_enclosures):
            print(f'{index + 1}. {enclosure.name} (Cleanliness: {enclosure.cleanliness})')
            enclosure_dictionary[str(index + 1)] = enclosure
        return enclosure_dictionary

    def menu_enclosures_by_cleanliness(self):
        '''Lists all enclosures sorted by their cleanliness level.'''
        print()
        # Sort enclosures using the 'cleanliness' attribute as the key
        enclosure_by_cleanliness = sorted(self.all_enclosures,
                                          key=lambda enclosure: enclosure.cleanliness)
        print('Enclosures by cleanliness:')
        for index, enclosure in enumerate(enclosure_by_cleanliness):
            print(f'{index + 1}. {enclosure.name} | Cleanliness: {enclosure.cleanliness}')

    def menu_enclosure_add(self):
        '''Prompts for details and adds a new enclosure to the zoo.'''
        print()
        name = input('Enter Enclosure Name: ').title()

        # Check for duplicate enclosure name
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

        # Create and initialize the new enclosure object
        new_enclosure = Enclosure.Enclosure(name, biome, area)
        new_enclosure.new_enclosure()

        # Add to master list and tracking list
        self.all_enclosures.append(new_enclosure)
        self._new_enclosures.append(new_enclosure)

        print(f'Successfully added {new_enclosure.name}!')

    def menu_enclosure_remove(self):
        '''Removes an enclosure from the zoo.'''
        print('\n--- Enclosure Closure ---')
        # List current enclosures for selection
        for enclosure in self.all_enclosures:
            print(f'{enclosure.name}')

        enclosure_to_remove = input('Which Enclosure do you want to close? ').title()
        enclosure_object_to_remove = None

        # Find the enclosure object by name
        for enclosure in self.all_enclosures:
            if enclosure.name == enclosure_to_remove:
                enclosure_object_to_remove = enclosure
                break

        if enclosure_object_to_remove:
            self.all_enclosures.remove(enclosure_object_to_remove) # Remove from master list
            print(f'Successfully removed {enclosure_object_to_remove.name}')
        else:
            print(f'Enclosure {enclosure_to_remove} not found.')

    def menu_animals(self):
        '''Holds the main Animal menu for selecting sub-menus'''
        print()
        print(self.animal_menu)
        animals_menu_input = input('Which Animals menu would you like to explore? ')

        # Direct to specific animal sub-menus based on input
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
        '''Lists all animals in the zoo with their ID and species.'''
        print('\nAll animals in the Zoo: ')
        for animal in self.all_animals:
            print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')

    def set_animals_by_diet(self):
        '''Intended to separate animals by diet.'''
        meat_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Meat':
                meat_diet.append(animal.name)
        plant_diet = []
        for animal in self.all_animals:
            if animal.diet == 'Plants':
                plant_diet.append(animal.name)

    def menu_animals_by_diet(self):
        '''Lists animals filtered by their diet type (Carnivore or Herbivore).'''
        diet_choice = input('\nWould you like to see:'
                            '\n1. Carnivores'
                            '\n2. Herbivores'
                            '\nSelection: ')

        # Filter and print Carnivores (Meat diet)
        if diet_choice == '1':
            for animal in self.all_animals:
                if animal.diet == 'Meat':
                    print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')
        # Filter and print Herbivores (Plants diet)
        elif diet_choice == '2':
            for animal in self.all_animals:
                if animal.diet == 'Plants':
                    print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')
        else:
            print('Invalid choice.')

    def menu_animals_by_biome(self):
        '''Lists animals that belong to a specific, user-chosen biome.'''
        print()
        # List available enclosures/biomes for the user to choose from
        for enclosure in self.all_enclosures:
            print(f'* {enclosure.name} | Biome: {enclosure.biome}')

        target_biome = input('Which biome\'s inhabitants do you want to check? ').capitalize()

        print(f'\n--- Animals in the {target_biome} Enclosure ---')
        # Find animals whose biome matches the target
        found = [animal for animal in self.all_animals if animal.biome == target_biome]

        if not found:
            print(f'No animals currently assigned to the {target_biome} enclosure.')
            return

        # Print the found animals
        for animal in found:
            print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')

    def menu_animals_health_card(self):
        '''Displays the health record/details of a selected animal.'''
        print('\n--- Animal Health Card Selection ---')

        # List all animals for the user to choose by ID
        for animal in self.all_animals:
            print(f'* ID: {animal.animal_id} | {animal.name} the {animal.species}')

        animal_selection_id = input('Enter the ID of the animal (e.g., A001): ').upper()

        # Find the animal and call its health_record method
        for animal in self.all_animals:
            if animal_selection_id == animal.animal_id:
                animal.health_record()
                return

        print(f'Invalid Selection: Animal ID {animal_selection_id} not found.')

    def menu_animals_add(self):
        '''Handles the process of acquiring a new animal and placing it in a suitable enclosure.'''
        print('\n--- Acquire New Animal ---')
        # Get the list of available species classes
        available_species = Animal.Animal.get_all_concrete_animal_types()
        print(f'Available Species: {', '.join(available_species)}')

        species_choice = input('Enter the Species name: ').title()
        name = input('Enter the Animal\'s Name (Leave blank for random): ')

        try:
            # Dynamically get the class and create the animal object
            animal_class = getattr(Animal, species_choice)
            new_animal = animal_class(name if name else None)

        except (AttributeError, TypeError):
            print(f'Invalid species: {species_choice} or creation error.')
            return

        suitable_enclosure = None
        print('Attempting placement in available enclosures...')

        # Attempt to add the new animal to the first suitable enclosure found
        for enclosure in self.all_enclosures:
            success, message = enclosure.add_animal(new_animal)

            if success:
                suitable_enclosure = enclosure
                # The loop continues to print all failure messages but only uses the first successful placement
            else:
                print(f'   - In {enclosure.name}: {message}')

        if suitable_enclosure:
            # Add to master list and tracking list upon successful placement
            self.all_animals.append(new_animal)
            self._new_animals.append(new_animal)
            print(
                f'New arrival! {new_animal.name} the {new_animal.species} is settling into {suitable_enclosure.name}.')
        else:
            print(f'Unable to home {new_animal.name}. No suitable enclosure found.'
                  f'\nAdd a new enclosure for this animal first.')

    def menu_animals_remove(self):
        '''Attempts to remove an animal, running all checks.'''
        print('\n--- Animal Release Menu ---')

        # List animals for user choice
        for animal in self.all_animals:
            print(f'*{animal.name} the {animal.species}')

        animal_to_remove_name = input('Which animal are we releasing from captivity? ').capitalize()
        animal_object_to_release = None

        # Find the animal object by name
        for animal in self.all_animals:
            if animal.name == animal_to_remove_name:
                animal_object_to_release = animal
                break

        if animal_object_to_release:
            self.all_animals.remove(animal_object_to_release) # Remove from master list

            # Remove the animal from its enclosure's list of animals
            for enclosure in self.all_enclosures:
                if animal_object_to_release in enclosure.animals:
                    enclosure.animals.remove(animal_object_to_release)
                    print(f'Removed {animal_object_to_release.name} from {enclosure.name}.')
            print(f'{animal_to_remove_name} was sent back to the wild! Goodbye...')
        else:
            print(f'Invalid Selection: Animal {animal_to_remove_name} not found.')

    def list_sick_animals(self, max_health=100):
        '''Lists animals below a max health threshold and returns a dict mapping selection ID to animal object.'''
        # Filter for animals with health less than the maximum
        sick_animals = [a for a in self.all_animals if a.health < max_health]
        if not sick_animals:
            print('All animals are healthy!')
            return None

        print(f'\n--- Animals Needing Medical Attention ---')
        animal_dictionary = {}
        for index, animal in enumerate(sick_animals):
            print(f'{index + 1}. ID: {animal.animal_id} | {animal.name} the {animal.species} (Health: {animal.health})')
            animal_dictionary[str(index + 1)] = animal
        return animal_dictionary

    def sick_animal(self):
        '''Handles the daily chance of an animal becoming sick.'''
        sickness_spread = False
        sick_animals = []

        # Check if any animal is already severely sick (health 0)
        for animal in self.all_animals:
            sick_animals.append(animal.name)
            if animal.health == 0:
                sickness_spread = True

        if sickness_spread:
            pass # Currently does nothing if sickness is spread

        if not sickness_spread:
            # 10% chance for a random animal to get sick
            sick_chance = random.randint(0, 100)
            if sick_chance >= 90:
                random_animal = random.choice(list(self.all_animals))
                random_animal.health = 0 # Set health to 0 (sick)
                print(f'{random_animal.name} is sick and needs to see a Vet')
            else:
                print('No animals became unhealthy overnight.. Phew!!')

if __name__ == '__main__':
    # Run the main program function
    main()