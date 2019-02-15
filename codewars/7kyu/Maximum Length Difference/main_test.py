import main
import unittest

class MaxTest(unittest.TestCase):
    def testing(self):
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        self.assertEqual(main.mxdiflg(s1, s2), 13)

if __name__ == '__main__':
    unittest.main()