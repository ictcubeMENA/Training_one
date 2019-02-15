import unittest

from main import count_animals


class Test_Dcount_animals(unittest.TestCase):

    def test(self):
        self.assertIsNotNone(count_animals("I see 3 zebras, 5 lions and 6 giraffes.") == 14, 'Live from the Savannah')
        self.assertIsNotNone(count_animals("Mom, 3 rhinoceros and 6 snakes come to us!"), 'Close the car !')
        self.assertIsNotNone(count_animals("I do not see any animals here!") == 0, 'Live from the kitchen')


if __name__ == '__main__':
    unittest.main()
