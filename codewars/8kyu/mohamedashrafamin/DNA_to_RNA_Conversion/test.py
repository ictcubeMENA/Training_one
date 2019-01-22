import unittest
from colorama import Fore
from main import DNAtoRNA


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(DNAtoRNA("TTTT"), "UUUU")
        print(Fore.GREEN + 'Test Passed')
        self.assertEqual(DNAtoRNA("GCAT"), "GCAU")
        print(Fore.GREEN + 'Test Passed')
        self.assertEqual(DNAtoRNA("GACCGCCGCC"), "GACCGCCGCC")
        print(Fore.GREEN + 'Test Passed')
        print(Fore.GREEN+"You have passed all of the tests! :)")


if __name__ == '__main__':
    unittest.main()
