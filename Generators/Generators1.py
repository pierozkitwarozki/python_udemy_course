# Explanation


def generate_func(num):
    for i in range(num):
        yield i  # not return, YIELD. It's simple to see the difference. You can return only ONCE,
        # but yield in each iteration


my_list = list(generate_func(100))
print(my_list)

gen = generate_func(100)
next(gen)  # first iteration - 0
next(gen)  # second iteration - 1
print(next(gen))  # third iteration - 2
