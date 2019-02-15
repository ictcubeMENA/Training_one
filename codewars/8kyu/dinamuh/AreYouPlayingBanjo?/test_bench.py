from main import areYouPlayingBanjo
from main import areYouPlayingBanjo2


def test(benchmark):
    assert benchmark(areYouPlayingBanjo, "martin") == "martin does not play banjo"


def test2(benchmark):
    assert benchmark(areYouPlayingBanjo2, "martin") == "martin does not play banjo"


''''''''''''''''
--------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
Name (time in ns)          Min                   Max                Mean             StdDev              Median               IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  208.0909 (1.0)      1,693.5000 (1.0)      222.2836 (1.0)      42.1379 (1.0)      216.0455 (1.0)      7.3182 (1.0)      4637;8129        4.4988 (1.0)      199204          22
test2                 279.2000 (1.34)     2,251.4000 (1.33)     297.6158 (1.34)     58.5519 (1.39)     286.1000 (1.32)     9.6000 (1.31)     4432;9129        3.3600 (0.75)     157953          20
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 4.69 seconds ===================================================
'''''''''''''''''''''''''''
