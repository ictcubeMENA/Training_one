import main
import unittest

class AnimalsTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.count_animals("I see 3 zebras, 5 lions and 6 giraffes."),14)
        self.assertEqual(main.count_animals("Mom, 3 rhinoceros and 6 snakes come to us!"),9)
        self.assertEqual(main.count_animals("I do not see any animals here!") , 0)

if __name__ == '__main__':
    unittest.main()

