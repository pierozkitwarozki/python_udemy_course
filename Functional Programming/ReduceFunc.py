from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


my_list = [1, 2, 3, 4, 5, 6]

print(reduce(accumulator, my_list,
             10))  # simple explanation: accumulator - a function; my_list - item; 10 - acc (default - 0)
