"""Homework 13

1. Using Import:

a. Create a file named my_func.py and insert the following function inside it:
def print_stars():
print('************')"""

#d. Add documentation to the stars_print function using.

"""The function print_starts prints a string of 12 starts (*)"""
def print_stars():
    print('************')

"""c. __name__ the printer print command my_func.py - to add
Now make sure that the print does not appear when doing import.
if __name__ == "__main__" hint"""

if __name__ == '__main__':
    print_stars()