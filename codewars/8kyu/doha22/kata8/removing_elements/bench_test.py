from removing_elements import remove_every_other
from removing_elements import remove_every_other2

def test(benchmark):
    assert benchmark(remove_every_other,['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again']



def test2(benchmark):
    assert benchmark(remove_every_other2, ['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again']

'''''''''
----------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                 Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.6421 (1.0)      355.5175 (1.0)      2.4519 (1.0)      3.6974 (1.0)      2.0526 (1.0)      0.4105 (1.0)      674;12507      407.8492 (1.0)       57998           1
test2                 4.1053 (2.50)     949.5518 (2.67)     6.7780 (2.76)     8.6116 (2.33)     4.9263 (2.40)     4.1053 (10.00)    1085;1189      147.5357 (0.36)      65835           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 7.33 seconds =================================================================================

'''''