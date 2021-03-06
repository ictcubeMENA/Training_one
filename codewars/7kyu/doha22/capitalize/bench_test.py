from capitalize import capitalize
from capitalize import capitalize2


def test(benchmark):
    assert benchmark(capitalize, "abcdef") == ['AbCdEf', 'aBcDeF']


def test2(benchmark):
    assert benchmark(capitalize2, "abcdef") == ['AbCdEf', 'aBcDeF']

'''''''''
------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------

Name (time in us)        Min                   Max               Mean             StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

test2                 6.9790 (1.0)        805.0469 (1.0)      12.0515 (1.0)      11.2096 (1.0)       8.2106 (1.0)      7.3895 (2.00)      462;383       82.9774 (1.0)       30073           1

test                  9.0316 (1.29)     4,384.0365 (5.45)     24.4851 (2.03)     69.8857 (6.23)     20.1159 (2.45)     3.6948 (1.0)      253;2874       40.8412 (0.49)      20999           1

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 3.87 seconds =================================================================================

'''''