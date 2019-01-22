import unittest
from main import remove


class TestSum(unittest.TestCase):

    tests = [
        # [[input], [expected]],
        [["Hi!", 1], "Hi"],
        [["Hi!", 100], "Hi"],
        [["Hi!!!", 1], "Hi!!"],
        [["Hi!!!", 100], "Hi"],
        [["!Hi", 1], "Hi"],
        [["!Hi!", 1], "Hi!"],
        [["!Hi!", 100], "Hi"],
        [["!!!Hi !!hi!!! !hi", 1], "!!Hi !!hi!!! !hi"],
        [["!!!Hi !!hi!!! !hi", 3], "Hi !!hi!!! !hi"],
        [["!!!Hi !!hi!!! !hi", 5], "Hi hi!!! !hi"],
        [["!!!Hi !!hi!!! !hi", 100], "Hi hi hi"],
    ]

    def test(self):
        for inp, exp in self.tests:
            self.assertEqual(remove(*inp), exp)


if __name__ == '__main__':
    unittest.main()
