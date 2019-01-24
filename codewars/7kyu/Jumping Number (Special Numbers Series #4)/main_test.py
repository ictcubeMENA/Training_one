import main
import unittest

class JumpingTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.jumping_number(1), "Jumping!!")
        self.assertEqual(main.jumping_number(7), "Jumping!!")
        self.assertEqual(main.jumping_number(9), "Jumping!!")
        self.assertEqual(main.jumping_number(23), "Jumping!!")
        self.assertEqual(main.jumping_number(32), "Jumping!!")
        self.assertEqual(main.jumping_number(79), "Not!!")
        self.assertEqual(main.jumping_number(98), "Jumping!!")
        self.assertEqual(main.jumping_number(8987)    , "Jumping!!")
        self.assertEqual(main.jumping_number(4343456) , "Jumping!!")
        self.assertEqual(main.jumping_number(98789876), "Jumping!!")

if __name__ == '__main__':
    unittest.main()
