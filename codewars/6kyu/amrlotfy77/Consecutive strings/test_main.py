import unittest

from main import longest_consec

class Test_capitalize(unittest.TestCase):






        def testing(self):
            self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")

            self.assertEqual(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2), "")
            self.assertEqual(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 3), "ixoyx3452zzzzzzzzzzzz")
            self.assertEqual(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 15), "")
            self.assertEqual(longest_consec(["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"], 0), "")

if __name__ == '__main__':
    unittest.main()