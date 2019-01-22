import unittest

from main import areYouPlayingBanjo

class Test_areYouPlayingBanjo(unittest.TestCase):





    def test(self):
        self.assertEqual(areYouPlayingBanjo("martin"), "martin does not play banjo");
        self.assertEqual(areYouPlayingBanjo("Rikke"), "Rikke plays banjo");

if __name__ == '__main__':
    unittest.main()