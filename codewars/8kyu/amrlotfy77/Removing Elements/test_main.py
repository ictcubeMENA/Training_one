import unittest

from main import remove_every_other

class Test_DNAtoRNA(unittest.TestCase):





    def test(self):




        self.assertEqual(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                           ['Hello', 'Hello Again'])
        self.assertEqual(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                           [1, 3, 5, 7, 9])
        self.assertEqual(remove_every_other([[1, 2]]), [[1, 2]])
        self.assertEqual(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                           [['Goodbye']])


if __name__ == '__main__':
    unittest.main()