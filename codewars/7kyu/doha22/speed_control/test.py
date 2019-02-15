import unittest
from speed_control import gps ,gps2


def test_gps(benchmark):
    assert benchmark(gps,17, [0.0, 0.02, 0.36, 0.54, 0.72, 0.9, 1.08, 1.26, 1.44, 1.62, 1.8]   ) == 72
    assert benchmark(gps2,12 , [0.0, 0.24, 0.48, 0.72, 0.96, 1.2, 1.44, 1.68, 1.92, 2.16, 2.4]  ) == 72
