import random
import sys

while True:
    try:
        first = int(input('insert first number: '))  # change to sys.argv[1] if able to run via terminal
        second = int(input('insert second number: '))  # change to sys.argv[2]
        break
    except ValueError:
        print('please insert a number...')

print('random number game\n'
      f'guess numbers from {first} to {second}')

num = random.randint(first, second)
users_num = -1
while users_num != num:
    try:
        users_num = int(input('guess the number: '))  # must be converted to int, because input is a string
        # print(f'answer: {num}\n\n')
    except ValueError:
        print('please insert a number...')

print('good job!')
