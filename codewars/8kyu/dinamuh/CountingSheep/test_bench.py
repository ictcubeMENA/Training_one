from main import count_sheeps
from main import count_sheeps2

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def test(benchmark):
    assert benchmark(count_sheeps, array1) == 17


def test2(benchmark):
    assert benchmark(count_sheeps2, array1) == 17


'''''''''''
-------------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------------
Name (time in ns)            Min                   Max                  Mean              StdDev                Median                IQR              Outliers  OPS (Kops/s)            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                   235.3000 (1.0)      3,291.8500 (1.0)        318.5801 (1.0)      136.9252 (1.0)        265.6500 (1.0)      63.5000 (2.13)    24361;25701    3,138.9276 (1.0)      195199          20
test                  1,033.0000 (4.39)     7,150.4000 (2.17)     1,136.4033 (3.57)     281.8505 (2.06)     1,083.0000 (4.08)     29.8000 (1.0)      5815;14224      879.9693 (0.28)     176523           5
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 5.18 seconds =======================
'''''''''''
