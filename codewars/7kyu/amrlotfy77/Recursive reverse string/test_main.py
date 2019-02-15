import unittest

from main import reverse


class Test_reverse(unittest.TestCase):

    def test(self):
        self.assertEqual("hello world", reverse("dlrow olleh"))


if __name__ == '__main__':
    unittest.main()
