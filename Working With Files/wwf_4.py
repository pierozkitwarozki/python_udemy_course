# always put working with files in try exception

try:
    with open('tests.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File not found')
    raise err
except IOError as err:
    print('IO Error')
    raise err
