import unittest
from main import scale
a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"


def test_scale(benchmark):
        assert benchmark(scale,a, 2, 3)== r
        assert benchmark(scale,"", 5, 5)== ""
        assert benchmark(scale,"Kj\nSH", 1, 2)=="Kj\nKj\nSH\nSH"

