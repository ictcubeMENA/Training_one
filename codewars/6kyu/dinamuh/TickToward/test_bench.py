from main import tick_toward
from main import tick_toward2


def test(benchmark):
    assert benchmark(tick_toward, (3, 2), (4, 5)) == [(3, 2), (4, 3), (4, 4), (4, 5)]


def test2(benchmark):
    assert benchmark(tick_toward2, (3, 2), (4, 5)) == [(3, 2), (4, 3), (4, 4), (4, 5)]


'''''''''''
----------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR              Outliers  OPS (Kops/s)            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 1.0056 (1.0)      12.0042 (1.0)      1.0558 (1.0)      0.1880 (1.0)      1.0294 (1.0)      0.0112 (1.0)      3085;12320      947.1675 (1.0)      186742           5
test                  1.5310 (1.52)     38.6300 (3.22)     1.6459 (1.56)     0.4000 (2.13)     1.6110 (1.56)     0.0460 (4.11)     1066;11330      607.5752 (0.64)     120788           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 3.66 seconds ==========================================================
'''''
