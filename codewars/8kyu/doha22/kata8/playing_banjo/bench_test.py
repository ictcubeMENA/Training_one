from playing_banjo import areYouPlayingBanjo
from playing_banjo import areYouPlayingBanjo2

def test(benchmark):
    assert benchmark(areYouPlayingBanjo,"martin") =="martin does not play banjo"



def test2(benchmark):
    assert benchmark(areYouPlayingBanjo2, "martin") == "martin does not play banjo"

''''''''''
------------------------------------------------------------------------------------ benchmark: 2 tests -----------------------------------------------------------------------------------
Name (time in us)        Min                   Max              Mean             StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 1.6421 (1.0)      6,912.0640 (8.42)     4.9729 (1.19)     28.1469 (4.93)     4.1053 (1.25)     2.4632 (6.00)     814;3402      201.0904 (0.84)     121795           1
test                  3.2842 (2.00)       820.6460 (1.0)      4.1807 (1.0)       5.7086 (1.0)      3.2842 (1.0)      0.4105 (1.0)      826;9068      239.1930 (1.0)       60898           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 9.18 seconds =================================================================================

'''''''''''