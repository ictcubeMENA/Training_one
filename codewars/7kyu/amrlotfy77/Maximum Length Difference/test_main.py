import unittest

from main import mxdiflg


class Test_mxdiflg(unittest.TestCase):

    def test(self):
        s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii",
              "dvvvwz"]
        s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
        self.assertEqual(mxdiflg(s1, s2), 13)


if __name__ == '__main__':
    unittest.main()
