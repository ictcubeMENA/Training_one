import unittest

from main import capitalize


class Test_capitalize(unittest.TestCase):

    def test(self):
        self.subTest("Basic tests")
        self.assertEqual(capitalize("abcdef"), ['AbCdEf', 'aBcDeF'])
        self.assertEqual(capitalize("codewars"), ['CoDeWaRs', 'cOdEwArS'])
        self.assertEqual(capitalize("abracadabra"), ['AbRaCaDaBrA', 'aBrAcAdAbRa'])
        self.assertEqual(capitalize("codewarriors"), ['CoDeWaRrIoRs', 'cOdEwArRiOrS'])


if __name__ == '__main__':
    unittest.main()
