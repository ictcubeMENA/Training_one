import main
import unittest
class altertest(unittest.TestCase):
    def testing(self):
        self.assertEqual(main.capitalize("abcdef"),['AbCdEf', 'aBcDeF'])
        self.assertEqual(main.capitalize("codewars"),['CoDeWaRs', 'cOdEwArS'])
        self.assertEqual(main.capitalize("abracadabra"),['AbRaCaDaBrA', 'aBrAcAdAbRa'])
        self.assertEqual(main.capitalize("codewarriors"),['CoDeWaRrIoRs', 'cOdEwArRiOrS'])

if __name__ == '__main__':
    unittest.main()