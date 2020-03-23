# Map function always returns the same amount of arguments as were given in input
# in opposite way, filter filters those arguments and only returns those which fulfill the condition
# in short: "If it's true, I'm gonna keep it in the list, if it's not i'm gonna throw it away


def check_even(item):
    return item % 2 == 0


print(f'Filter function: {list(filter(check_even, [1, 2, 3, 4, 5, 6, 7]))}')
print(f'Map function: {list(map(check_even, [1, 2, 3, 4, 5, 6, 7]))}')
