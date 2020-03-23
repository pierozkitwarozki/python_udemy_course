# Quick note - HOF - Higher Order Function - Function that uses another function (as a parameter or return it)
# Example should show how it works


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('started wrapping param function')
        func(*args, **kwargs)
        print('wrapping completed', end='\n\n')

    return wrap_func


@my_decorator
def hello_func(name):
    print(f'Hi my name is {name}')


@my_decorator
def bye_func(name):
    print(f'Bye Bye {name}')


hello_func('Slim Shady')
bye_func('Folks')
