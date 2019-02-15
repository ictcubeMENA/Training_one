import unittest

from main import camel_case

class Test_camel_case(unittest.TestCase):





    def test(self):

        self.subTest("Basic tests")
        self.assertEqual(camel_case("test case"), "TestCase")
        self.assertEqual(camel_case("camel case method"), "CamelCaseMethod")
        self.assertEqual(camel_case("say hello "), "SayHello")
        self.assertEqual(camel_case(" camel case word"), "CamelCaseWord")
        self.assertEqual(camel_case(""), "")

if __name__ == '__main__':
    unittest.main()