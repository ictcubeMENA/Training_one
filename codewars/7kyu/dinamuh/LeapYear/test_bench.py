from main import isLeapYear
from main import isLeapYear2


def test(benchmark):
    assert benchmark(isLeapYear, 2000) == True, 'Year 2000 was a leap year!'


def test2(benchmark):
    assert benchmark(isLeapYear2, 2000) == True, 'Year 2000 was a leap year!'


'''''''''
-------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
Name (time in ns)          Min                 Max                Mean             StdDev              Median               IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  149.7400 (1.0)      571.4700 (1.0)      153.9809 (1.0)      15.9465 (1.0)      151.2700 (1.0)      0.6800 (1.0)      1760;6300        6.4943 (1.0)       63072         100
test2                 156.1600 (1.04)     597.3100 (1.05)     162.5421 (1.06)     21.4012 (1.34)     157.5700 (1.04)     0.8500 (1.25)    1583;10097        6.1523 (0.95)      61358         100
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 3.57 seconds ==========================================
'''''''''''''''