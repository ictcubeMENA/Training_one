from main import sum_fracts
from main import sum_fracts2

def test(benchmark):
    assert benchmark(sum_fracts, [[1, 3], [5, 3]]) == 2


def test2(benchmark):
    assert benchmark(sum_fracts2, [[1, 3], [5, 3]]) == 2





'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.9300 (1.0)      54.2360 (1.87)     2.0925 (1.0)      0.5985 (1.0)      2.0180 (1.0)      0.0620 (1.0)     1065;3516      477.9071 (1.0)       51841           1
test2                 8.6050 (4.46)     28.9640 (1.0)      9.1972 (4.40)     1.3333 (2.23)     8.9520 (4.44)     0.1450 (2.34)      523;912      108.7287 (0.23)      11723           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 1.54 seconds ===================================================================
'''''''''''''''''