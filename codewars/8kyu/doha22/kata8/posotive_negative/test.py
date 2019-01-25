import unittest
from positive_negative import count_positives_sum_negatives


def test_count_positives_sum_negatives(benchmark):
    assert benchmark(count_positives_sum_negatives,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14,-15])==[10,-65]
    assert benchmark(count_positives_sum_negatives,[1]) == [1,0]
