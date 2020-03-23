from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def capitalize_item(item):
    return item.capitalize()


def filter_score(item):
    return item > 50


def accumulator(acc, item):
    return acc + item


print(f'#1 capitalized: {list(map(capitalize_item, my_pets))}')

print(f'#2 zipped sorted: {list(zip(my_strings, sorted(my_numbers)))}')

print(f'#3 scores over 50%: {list(filter(filter_score, sorted(scores)))}')

print(f'#4 total is: {reduce(accumulator, scores + my_numbers, 0)}')
