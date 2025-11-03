'''
File: Staff.py
Description: This module contains the permisible enclosure types for the animals ant their status
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''



class Enclosure:
    def __init__(self, name, cleanliness=100, size=None):
        self.name = name
        self.cleanliness = cleanliness
        self.size = size

