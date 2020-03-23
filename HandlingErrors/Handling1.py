# Easy readable code, no need to explain anything

while True:
    try:
        age = int(input('Enter your age: '))
        result = 10 / age
        print(age)
        # raise ValueError - throwing an error
    except ZeroDivisionError as error:
        print(f'Please enter number higher than 0!\n'
              f'{error}')
    except ValueError as error:
        print(f'Please enter a number.\n'
              f'{error}')
    else:
        print('Thank you')  # running only without error
    finally:
        print('thank you')  # running every time
