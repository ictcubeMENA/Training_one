from main import mxdiflg

s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]


def test(benchmark):
    assert benchmark(mxdiflg, s1, s2) == 13


def test2(benchmark):
    assert benchmark(mxdiflg, s1, s2) == 13


'''''''''
----------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR              Outliers  OPS (Kops/s)            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 1.5680 (1.0)      14.5567 (1.0)      1.6544 (1.0)      0.2915 (1.0)      1.6000 (1.0)      0.0470 (1.0)      4665;18920      604.4431 (1.0)      178604           3
test                  1.6260 (1.04)     32.2320 (2.21)     1.7490 (1.06)     0.5048 (1.73)     1.6840 (1.05)     0.0500 (1.06)      2163;5781      571.7588 (0.95)     126663           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 3.54 seconds =======================
'''''''''''
