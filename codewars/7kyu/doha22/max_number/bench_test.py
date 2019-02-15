from max_number import max_number
from max_number import max_number2


def test(benchmark):
    assert benchmark(max_number, 213) == 321


def test2(benchmark):
    assert benchmark(max_number2, 213) == 321

 '''''''''''  
 ------------------------------------------------------------------------------------ benchmark: 2 tests ------------------------------------------------------------------------------------
Name (time in us)        Min                    Max              Mean             StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  2.4632 (1.0)       8,918.3265 (1.0)      6.1721 (1.0)      47.6550 (1.0)      5.3369 (1.0)      1.2316 (1.50)     115;8488      162.0182 (1.0)       45109           1
test2                 2.4632 (1.0)      10,636.3894 (1.19)     7.5089 (1.22)     89.8274 (1.88)     5.3369 (1.0)      0.8211 (1.0)      131;5922      133.1753 (0.82)      59412           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 4.03 seconds =================================================================================

''''
