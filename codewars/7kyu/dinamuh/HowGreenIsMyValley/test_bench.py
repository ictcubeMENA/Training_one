from main import make_valley
from main import make_valley2


def test(benchmark):
    assert benchmark(make_valley, [20, 7, 6, 2]) == [20, 6, 2, 7]


def test2(benchmark):
    assert benchmark(make_valley2, [20, 7, 6, 2]) == [20, 6, 2, 7]


'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 1.1460 (1.0)      17.2630 (1.32)     1.2392 (1.0)      0.3518 (1.02)     1.2090 (1.0)      0.0390 (1.0)      743;8864      806.9926 (1.0)      103574           1
test                  1.2040 (1.05)     13.0350 (1.0)      1.3078 (1.06)     0.3460 (1.0)      1.2700 (1.05)     0.0460 (1.18)   1719;14570      764.6685 (0.95)     124720           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.35 seconds ==========================
'''''''''''
