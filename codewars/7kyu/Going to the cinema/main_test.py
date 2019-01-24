import main
import unittest

class CinemaTest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.movie(500, 15, 0.9), 43)
        self.assertEqual(main.movie(100, 10, 0.95), 24)

if __name__ == '__main__':
    unittest.main()