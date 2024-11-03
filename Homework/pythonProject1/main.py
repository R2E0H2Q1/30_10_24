"""b. Create another file named main.py and inside it - use Import to call the function
in the my_func.py file. Run the function 5 times in a loop

i. Solved using import to the entire file
ii. Solve using from to import only the stars_print function"""

from my_func import print_stars

for _ in range(5):
    print_stars()

#Now in main.py call the help function to see an explanation of the my_func functions
help(print_stars())