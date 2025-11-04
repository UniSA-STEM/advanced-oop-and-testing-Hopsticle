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

class ZooManager():
    def __init__(self, all_staff):
        self.staff = all_staff

    def add_staff(self):
        new_staff = Staff.Staff(name=random.choice(Staff.names))
        print(new_staff)
        all_staff.append(new_staff)

ZooManager(all_staff)
