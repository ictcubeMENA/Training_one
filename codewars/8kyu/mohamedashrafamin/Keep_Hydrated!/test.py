import unittest
from main import litres


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(litres(2), 1, 'should return 1 litre')
        self.assertEqual(litres(1.4), 0, 'should return 0 litres')
        self.assertEqual(litres(12.3), 6, 'should return 6 litres')
        self.assertEqual(litres(0.82), 0, 'should return 0 litres')
        self.assertEqual(litres(11.8), 5, 'should return 5 litres')
        self.assertEqual(litres(1787), 893, 'should return 893 litres')
        self.assertEqual(litres(0), 0, 'should return 0 litres')


if __name__ == '__main__':
    unittest.main()
