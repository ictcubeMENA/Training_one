import main
import unittest

class testsheep(unittest.TestCase):
    def testing(self):
        array1 = [True,  True,  True,  False,
              True,  True,  True,  True ,
              True,  False, True,  False,
              True,  False, False, True ,
              True,  True,  True,  True ,
              False, False, True,  True ];
              
       self.assertEqual(main.count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))

if __name__ == '__main__':
    unittest.main()