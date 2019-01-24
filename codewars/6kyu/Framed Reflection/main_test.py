import main
import unittest

class Framedreftest(unittest.TestCase):
    def framed_test(self):
        self.assertEqual(main.mirror("Hello World"), "*********\n* olleH *\n* dlroW *\n*********")
        self.assertEqual(main.mirror("Codewars"), "************\n* srawedoC *\n************")

if __name__ == '__main__':
    unittest.main()