# Checks how long did the func lasted

from time import time


def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'process took {t2 - t1} milliseconds.')
        return result

    return wrapper


@performance
def do_something():
    for item in range(1000000):
        item * 5


do_something()
