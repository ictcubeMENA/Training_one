from two_sum import two_sum
from two_sum import two_sum2


def test(benchmark):
    assert benchmark(two_sum, [1,2,3], 4) == [0,2]


def test2(benchmark):
    assert benchmark(two_sum2, [1,2,3], 4) == [0,2]

'''''''''''   
-------------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------
--
Name (time in us)        Min                    Max               Mean              StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iteratio
ns
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--
test2                 2.4632 (1.0)       2,032.1173 (1.0)       6.0053 (1.0)       12.9942 (1.0)       5.3369 (1.0)      3.2842 (1.0)      967;1481      166.5197 (1.0)       90218
 1
test                  6.5685 (2.67)     16,717.1412 (8.23)     16.3353 (2.72)     116.3888 (8.96)     13.9580 (2.62)     9.0316 (2.75)       95;723       61.2172 (0.37)      25113
 1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 5.59 seconds =================================================================================

'''''''' 
