import main
import unittest

class ComposeTest(unittest.TestCase):
    def testing(self):   
        self.assertEqual(main.compose("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"), 
            "bNkTB\nhTrWO\nRTFVi\nCnnIj")
        self.assertEqual(main.compose("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"), 
            "HgYPW\nTGGbM\nIPhqt\nuUMDH")

if __name__ == '__main__':
    unittest.main()


