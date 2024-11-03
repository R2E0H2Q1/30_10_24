"""2. Rehearsal exercises for the test (authority):

a. 30 students can enter a study class. The school has 103 students
How many full classes of 30 students will there be, and how many students will remain in the last class"""

students = 30
school = 103

rooms = school // students #Using operator // we will divide the two numbers and rounds down the # to a whole #.
print(f' You have {rooms} full classrooms with {students} students each.')

re_students = school % students

print(f'The forth class room contains only: {re_students} students.')

"""Now, instead of 103, take the number of students from the user and print some full classes
of 30 students will be, and some students will remain in the last class
Hint: use division and remainder %"""

amount_students: int = int(input('Enter the amount of students for the new school year: '))

how_many_rooms = amount_students // students
print(f'This year we have {how_many_rooms} classrooms of {students} students each.')

re_students2 = amount_students % students
print(f'In the last classroom you find only {re_students2} students.')

"""b. Record a number from the user, until a valid number between 10-99 is recorded (if you record a string).
The program will know how to handle the error...(Check if the one digit is greater than the tens digit."""


while True:
        num = input('Enter a number between 10-99: ')
        if num.isdigit() and 10 <= int(num) <= 99:
            num = int(num)
            break
        else:
            print("Invalid, number must be between 10 and 99.")

"""If so, reverse the number, if not, leave the number as it is.
- For example:
For the number 57, the answer will be 75
For the number 82, the answer will be 28
For the number 55, the answer will be 55"""

num_reversed = 0

while num > 0:
    digit = num % 10
    num_reversed = num_reversed * 10 + digit
    num //= 10

print(f'The reversed number of the one you entered is: {num_reversed}')

# """c. Print all prime numbers between 1-200
# a b c d Answers 4 There is an American for question d
# Receive answers from the user in a loop until the character x (to exit) is received
# (If a character other than x d c b a is received, receive again)
# At the end of the loop (after selecting x):
# Print How many students answered a, how many b, how many c, how many d?
# Print which answer is repeated the most times among d c b a? Which one is the least?"""

list_prime = []
for prime in range(1, 200 + 1):
    if prime < 2:
        continue
    is_prime = True

    list_prime.append(prime)
print(f'The list of prime numbers is: {list_prime}', end=' ')