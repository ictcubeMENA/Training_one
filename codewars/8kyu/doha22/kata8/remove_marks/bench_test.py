from remove_marks import remove_exclamation_marks
from remove_marks import remove_exclamation_marks2

def test(benchmark):
    assert benchmark(remove_exclamation_marks,"Hello World!") == "Hello World"



def test2(benchmark):
    assert benchmark(remove_exclamation_marks2,"Hello World!") == "Hello World"

''''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                 Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  2.0526 (1.0)      851.0250 (2.20)     3.0298 (1.0)      5.6253 (1.06)     2.4632 (1.0)      0.0000 (1.0)     625;27867      330.0502 (1.0)       76122           1
test2                 6.1579 (3.00)     387.5387 (1.0)      7.6990 (2.54)     5.3161 (1.0)      6.5685 (2.67)     0.4105 (>1000.0)  880;6829      129.8874 (0.39)      41999           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 6.76 seconds =================================================================================

'''''''''