# map does iteration for you, in short

def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, [1, 2, 3, 4, 5, 6])))
print(tuple(map(multiply_by_2, (1, 2, 3, 4))))
print(set(map(multiply_by_2, {1, 2, 3, 4})))
