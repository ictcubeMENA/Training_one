import unittest

from main import capitalizeWord

class Test_capitalizeWord(unittest.TestCase):





    def test(self):

        self.assertEqual(capitalizeWord('word'), 'Word');
        self.assertEqual(capitalizeWord('i'), 'I');
        self.assertEqual(capitalizeWord('glasswear'), 'Glasswear');
if __name__ == '__main__':
    unittest.main()