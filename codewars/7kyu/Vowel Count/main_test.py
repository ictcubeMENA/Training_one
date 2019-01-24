import main
import unittest

class voweltest(unittest.TestCase):
    def testing(self):
         self.assertEqual(main.getCount("abracadabra"), 5)
if __name__ == '__main__':
   unittest.main()         