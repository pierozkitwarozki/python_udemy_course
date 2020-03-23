# import random as bartolomeo
import random


# help(random) shows documentation of the module
# dir(random) prints functions included in the module

print(random.randint(0, 10))  # Examples
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8]))
my_list = [1, 2, 3, 4, 5, 6]
random.shuffle(my_list)
print(my_list)
