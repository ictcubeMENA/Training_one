from shortest_word import find_short
from shortest_word import find_short ,find_short2


def test(benchmark):
    assert benchmark(find_short, "bitcoin take over the world maybe who knows perhaps") == 3


def test2(benchmark):
    assert benchmark(find_short2, "bitcoin take over the world maybe who knows perhaps") == 3

''''''''''
------------------------------------------------------------------------------------- benchmark: 2 tests ------------------------------------------------------------------------------------
-
Name (time in us)        Min                    Max               Mean             StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iteration
s
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-
test2                 6.5685 (1.0)       6,063.5096 (1.0)      21.9342 (1.42)     88.4357 (1.0)      14.7790 (1.06)     3.2842 (1.0)      351;2683       45.5909 (0.71)      29348
1
test                  7.3895 (1.12)     10,243.5133 (1.69)     15.4903 (1.0)      94.9479 (1.07)     13.9580 (1.0)      7.3895 (2.25)      101;658       64.5564 (1.0)       25914
1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 4.43 seconds =================================================================================

'''''''''