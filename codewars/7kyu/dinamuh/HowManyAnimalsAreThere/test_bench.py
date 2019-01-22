from main import count_animals
from main import CountAnimals

def test(benchmark):
    assert benchmark(count_animals, "I see 3 zebras, 5 lions and 6 giraffes.") == 14, 'Live from the Savannah'


def test2(benchmark):
    assert benchmark(CountAnimals, "I see 3 zebras, 5 lions and 6 giraffes.") == 14, 'Live from the Savannah'










'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.4060 (1.0)      34.3320 (1.69)     1.5086 (1.0)      0.4598 (1.0)      1.4650 (1.0)      0.0480 (1.0)      799;4844      662.8847 (1.0)       78765           1
test2                 2.4600 (1.75)     20.3130 (1.0)      2.7748 (1.84)     0.7278 (1.58)     2.5790 (1.76)     0.1305 (2.72)     329;1399      360.3891 (0.54)       8856           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 1.58 seconds =============================
'''''''''