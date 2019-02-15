import unittest

from colorama import Fore

from main import is_opposite


class TestSum(unittest.TestCase):

    def test(self):
        self.assertEqual(is_opposite("ab", "AB"), True)
        print(Fore.GREEN + 'Test Passed')
        self.assertEqual(is_opposite("aB", "Ab"), True)
        print(Fore.GREEN + 'Test Passed')
        self.assertEqual(is_opposite("aBcd", "AbCD"), True)
        print(Fore.GREEN + 'Test Passed')
        self.assertEqual(is_opposite("AB", "Ab"), False)
        print(Fore.GREEN + 'Test Passed')
        self.assertEqual(is_opposite("", ""), False)
        print(Fore.GREEN + 'Test Passed')
        print(Fore.GREEN + "You have passed all of the tests! :)")


if __name__ == '__main__':
    unittest.main()
