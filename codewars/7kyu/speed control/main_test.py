import main
from math import floor, fabs
import unittest

class speedtest(unittest.TestCase):
    def testing(self):
        x = [0.0, 0.23, 0.46, 0.69, 0.92, 1.15, 1.38, 1.61]
        s = 20
        u = 41
        self.assertEqual(main.gps(s, x), u)
        x = [0.0, 0.11, 0.22, 0.33, 0.44, 0.65, 1.08, 1.26, 1.68, 1.89, 2.1, 2.31, 2.52, 3.25]
        s = 12
        u = 219
        self.assertEqual(main.gps(s, x), u)
        x = [0.0, 0.18, 0.36, 0.54, 0.72, 1.05, 1.26, 1.47, 1.92, 2.16, 2.4, 2.64, 2.88, 3.12, 3.36, 3.6, 3.84]
        s = 20
        u = 80
        self.assertEqual(main.gps(s, x), u)
        x = [0.0, 0.01, 0.36, 0.6, 0.84, 1.05, 1.26, 1.47, 1.68, 1.89, 2.1, 2.31, 2.52, 2.73, 2.94, 3.15]
        s = 14
        u = 90
        self.assertEqual(main.gps(s, x), u)
        x = [0.0, 0.02, 0.36, 0.54, 0.72, 0.9, 1.08, 1.26, 1.44, 1.62, 1.8]
        s = 17
        u = 72
        self.assertEqual(main.gps(s, x), u)

if __name__ == '__main__':
    unittest.main() 
