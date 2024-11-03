#How to import? from (source name file) import (function name file)

#1.Create a function called print_hello that print 'my first function'
#2. Call the function print_hello() 3 times in a for loop
#3. Create a new py file, inside the new file import the function and call it
#4. To do debugging and press step into and step out

def print_hello():
    print('My first function!')

for i in range(3):
    print_hello()


def get_int():
    x: int = 0
    while True:
        try:
            x = int(input('Enter a number: '))
            break
        except:
            print()

#In the python file with the print hello func 'add an explanation of it'.
#Add another function get_int which inputs a number and add a 'explanation of it too'
#after the import, in main, help (<func1>) help(<mod>)

print('[importEx301024] Whats your name? ', __name__)