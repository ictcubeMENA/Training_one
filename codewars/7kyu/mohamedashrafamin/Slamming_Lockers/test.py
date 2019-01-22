import unittest
from main import locker_run


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(locker_run(1), [1])


if __name__ == '__main__':
    unittest.main()
