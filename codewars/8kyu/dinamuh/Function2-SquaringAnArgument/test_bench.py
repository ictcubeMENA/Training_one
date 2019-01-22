from main import square
from main import square2


def test(benchmark):
    assert benchmark(square, 2) == 4


def test2(benchmark):
    assert benchmark(square2, 2) == 4


'''''''''
---------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
Name (time in ns)          Min                   Max                Mean             StdDev              Median               IQR              Outliers  OPS (Mops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  276.9412 (1.0)      3,014.4706 (1.34)     290.5854 (1.0)      49.1809 (1.20)     282.0588 (1.0)      2.4118 (1.0)      5864;18200        3.4413 (1.0)      199164          17
test2                 277.2778 (1.00)     2,242.4444 (1.0)      293.2404 (1.01)     41.0350 (1.0)      286.0000 (1.01)     4.4444 (1.84)     4481;23280        3.4102 (0.99)     196426          18
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 4.90 seconds ==========================================================
'''''''''
