import unittest

from main import reverse

class Test_reverse(unittest.TestCase):





    def test(self):

        self.assertEqual(
            reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]),
            ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]
        )

        self.assertEqual(
            reverse(
                ["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir",
                 "hsyn", "amwoH"]),
            ["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts", "to",
             "turn", "pink?"]
        )

if __name__ == '__main__':
    unittest.main()