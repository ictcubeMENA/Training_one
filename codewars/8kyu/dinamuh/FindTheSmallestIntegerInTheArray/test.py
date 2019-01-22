import unittest
from main import find_smallest_int



def test_find_smallest_int(benchmark):
         assert benchmark(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
         assert benchmark(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
         assert benchmark(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)

