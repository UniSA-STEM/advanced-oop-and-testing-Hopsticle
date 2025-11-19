'''
File: Utilities.py
Description: This module contains a number of commands that can stored and pulled from outside of the working modules
Author: Joshua Cordner
ID: corjy027
Username: corjy027
This is my own work as defined by the University's Academic Integrity Policy.
'''

import random

def load_names(filename='Names'):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print('Names file not found.')
        return []
names = load_names()

def get_random_name():
    return random.choice(names)
