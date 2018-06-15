#magic numbers
import random

magic_numbers = [random.randint(0,9), random.randint(0,9)]

# method
def ask_user_and_check():
    user_number = int(input('Enter your number'))
    if user_number in magic_numbers:
        return 'You got it'
    else:
        return 'You didn\'t get it'

def run_program_x_times(chances):
    for attemt in range(chances):
        print('This is attempt {}'.format(attemt))
        message = ask_user_and_check()
        print(message)

chances = int(input('How many chances you need?'))
run_program_x_times(chances)
