import unittest
import main_1


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main_1.do_stuff(test_param)
        self.assertEqual(result, 15)

    # def test_do_stuff2(self):
    #   test_param = 'word'
    #  result = main_1.do_stuff(test_param)
    # self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main_1.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main_1.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')


if __name__ == '__main__':
    unittest.main()
