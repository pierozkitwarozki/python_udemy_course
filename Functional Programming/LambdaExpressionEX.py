# Square of each item in a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda item: pow(item, 2), my_list)))

# Sorting by second item in the tuple, in the list
list_of_tuples = [(1, 2), (10, -1), (3, 55), (17, 0)]
list_of_tuples.sort(key=lambda x: x[1])
print(list_of_tuples)
