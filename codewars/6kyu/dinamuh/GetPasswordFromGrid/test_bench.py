from main import get_password
from main import get_password2

grid = [
    ["x", "l", "m"],
    ["o", "f", "c"],
    ["k", "i", "t"]
]
directions = ["rightT", "down", "leftT", "right", "rightT", "down", "left", "leftT"]


def test(benchmark):
    assert benchmark(get_password, grid, directions) == "lock"


def test2(benchmark):
    assert benchmark(get_password2, grid, directions) == "lock"


''''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  3.3790 (1.0)      29.7940 (1.0)      3.5974 (1.0)      0.7672 (1.0)      3.5020 (1.0)      0.0530 (1.0)      1448;6169      277.9805 (1.0)       71840           1
test2                 3.8290 (1.13)     35.5350 (1.19)     4.0865 (1.14)     0.8164 (1.06)     3.9790 (1.14)     0.0930 (1.75)     1769;3982      244.7071 (0.88)      92158           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.40 seconds ==========================================================
'''''
