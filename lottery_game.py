import random

# User can pick 6 numbers
def get_player_numbers():
    user_input = input('Enter 6 numbers, separated by commas')
    # split the input into a list
    numbers_list = user_input.split(',')
    # set comprehension
    interger_set = {int(number) for number in numbers_list}
    return interger_set

# Lottery calculates 6 random numbers b/w 1,20
def create_lottery_numbers():
    values = set() # cannot initialize like {}
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values

# match the lottery numbers to the user_numbers
def start():
    lottery_numbers = create_lottery_numbers()
    player_numbers = get_player_numbers()
    matches = lottery_numbers.intersection(player_numbers)
    print('Player numbers {}'.format(player_numbers))
    print('Lottery numbers {}'.format(lottery_numbers))
    print('You matched {} and won ${}!'.format(matches, 100*len(matches)))

start()
