import main
import unittest

class PassphrasesTest(unittest.TestCase):
    def pass_test(self):
        self.assertEqual(main.play_pass("I LOVE YOU!!!", 1), "!!!vPz fWpM J")
        self.assertEqual(main.play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2), 
            "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO")

if __name__ == '__main__':
    unittest.main()