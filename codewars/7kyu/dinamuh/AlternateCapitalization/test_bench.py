from main import capitalize
from main import capitalize2


def test(benchmark):
    assert benchmark(capitalize, "codewars") == ['CoDeWaRs', 'cOdEwArS']


def test2(benchmark):
    assert benchmark(capitalize2, "codewars") == ['CoDeWaRs', 'cOdEwArS']


'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 1.7870 (1.0)      18.8800 (1.0)      1.9624 (1.0)      0.4993 (1.0)      1.9190 (1.0)      0.0710 (2.09)     1888;5186      509.5727 (1.0)      132767           1
test                  2.7030 (1.51)     20.7530 (1.10)     2.8292 (1.44)     0.5116 (1.02)     2.7720 (1.44)     0.0340 (1.0)      2022;6001      353.4542 (0.69)      91870           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.57 seconds =======================================================
'''''''''''
