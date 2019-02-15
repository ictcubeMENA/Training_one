from no_space import no_space
from no_space import no_space2

def test(benchmark):
    assert benchmark(no_space,'8 j 8   mBliB8g  imjB8B8  jl  B' ) == '8j8mBliB8gimjB8B8jlB'



def test2(benchmark):
    assert benchmark(no_space2, '8 j 8   mBliB8g  imjB8B8  jl  B'  ) == '8j8mBliB8gimjB8B8jlB'


'''''''''''''''
----------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                 Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  2.8737 (1.0)      467.1811 (1.04)     3.9009 (1.0)      4.2598 (1.0)      3.2842 (1.0)      0.0000 (1.0)      643;21866      256.3500 (1.0)       50748           1
test2                 3.2842 (1.14)     451.1705 (1.0)      4.4991 (1.15)     5.0171 (1.18)     3.6948 (1.12)     0.0000 (2.00)    1239;32285      222.2643 (0.87)      86996           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 7.72 seconds =================================================================================

'''''''''''''''