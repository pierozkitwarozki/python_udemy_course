# Fibonacci generator


def fib(num):
    a = 0  # value for index 0
    b = 1  # value for index 1
    for i in range(num + 1):
        yield a
        temp = a
        a = b
        b = temp + b


def fib_list(num):
    a = 0
    b = 1
    my_list2 = []
    for i in range(num + 1):
        my_list2.append(a)
        temp = a
        a = b
        b = temp + b

    return my_list2


my_list = list(fib(8))
my_list3 = fib_list(8)
print(my_list3)
