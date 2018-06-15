user_input = input('Enter 6 numbers separated by comma')
user_numbers = user_input.split(',')
user_numbers_as_int = []
for number in user_numbers:
    user_numbers_as_int.append(int(number))

# List comprehension

print([int(number) for number in user_numbers])

# set

numbers = set()
numbers.add(4)

lottery_numbers = {3, 4, 5, 7}
user_list = {2, 3, 8, 0}

print(lottery_numbers.intersection(user_list))