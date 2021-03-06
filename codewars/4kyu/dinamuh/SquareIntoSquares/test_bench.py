from main import decompose
from main import decompose2


def test(benchmark):
    assert benchmark(decompose, 5) == [3, 4]


def test2(benchmark):
    assert benchmark(decompose2, 5) == [3, 4]


'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.1290 (1.0)      12.9650 (1.0)      1.2070 (1.0)      0.2362 (1.0)      1.1900 (1.0)      0.0230 (1.0)      1203;4325      828.4878 (1.0)      122026           1
test2                 2.0980 (1.86)     32.3090 (2.49)     2.2388 (1.85)     0.4605 (1.95)     2.1970 (1.85)     0.0300 (1.30)     2014;6523      446.6719 (0.54)     143103           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.68 seconds =================================================
'''''''''
