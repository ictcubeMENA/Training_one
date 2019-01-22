
import unittest
from main import movie



def test_movie(benchmark):
        assert benchmark(movie,500, 15, 0.9)== 43
        assert benchmark(movie,100, 10, 0.95)== 24
