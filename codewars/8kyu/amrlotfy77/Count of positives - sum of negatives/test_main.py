import unittest

from main import count_positives_sum_negatives

class Test_count_positives_sum_negatives(unittest.TestCase):





    def test(self):




        self.assertEqual(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),
                           [10, -65])
        self.assertEqual(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
        self.assertEqual(count_positives_sum_negatives([1]), [1, 0])
        self.assertEqual(count_positives_sum_negatives([-1]), [0, -1])
        self.assertEqual(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
        self.assertEqual(count_positives_sum_negatives([]), [])

if __name__ == '__main__':
    unittest.main()