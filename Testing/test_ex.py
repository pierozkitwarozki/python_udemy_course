import unittest
import exercise


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = exercise.run_guess_game(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        answer = 7
        guess = 3
        result = exercise.run_guess_game(guess, answer)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        answer = 5
        guess = 12
        result = exercise.run_guess_game(guess, answer)
        self.assertFalse(result)

    def test_input_string(self):
        answer = '5'
        guess = 5
        result = exercise.run_guess_game(guess, answer)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
