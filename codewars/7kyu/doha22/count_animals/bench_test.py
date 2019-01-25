from count_animals import count_animals
from count_animals import CountAnimals2


def test(benchmark):
    assert benchmark(count_animals, "I see 3 zebras, 5 lions and 6 giraffes.") == 14


def test2(benchmark):
    assert benchmark(CountAnimals2, "I see 3 zebras, 5 lions and 6 giraffes.") == 14

'''''''''''
----------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                 Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  4.1053 (1.0)      124.3902 (1.0)      5.1204 (1.0)      2.5556 (1.0)      4.5158 (1.0)      0.4105 (1.0)      5775;7279      195.2970 (1.0)       44289           1
test2                 4.5158 (1.10)     470.8765 (3.79)     7.0361 (1.37)     4.5951 (1.80)     5.3369 (1.18)     4.9263 (12.00)     5745;315      142.1235 (0.73)      69597           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 4.02 seconds =================================================================================

'''''''