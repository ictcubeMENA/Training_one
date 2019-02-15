import main
import unittest
class banjotest(unittest.TestCase):
    def testing(self):
        self.assertEqual(areYouPlayingBanjo("martin"), "martin does not play banjo")
        self.assertEqual(areYouPlayingBanjo("Rikke"), "Rikke plays banjo")

if __name__ == '__main__':
    unittest.main()