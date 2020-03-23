import random


def run_guess_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('congrats!')
            return True
    else:
        print('select from 1 to 10!')
        return False


if __name__ == '__main__':  # so game doesn't run while testing
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess the number from 1 to 10: '))
            if run_guess_game(guess, answer):
                break
        except ValueError:
            print('please enter a number: ')
            continue
