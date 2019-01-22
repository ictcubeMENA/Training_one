from main import case_sensitive
from main import case_sensitive2


def test(benchmark):
    assert benchmark(case_sensitive, 'cellS') == [False, ['S']]


def test2(benchmark):
    assert benchmark(case_sensitive2, 'cellS') == [False, ['S']]


'''''''''

----------------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------------
Name (time in ns)          Min                    Max                Mean              StdDev              Median                IQR              Outliers  OPS (Mops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 649.2500 (1.0)       2,961.6000 (1.0)      702.5583 (1.0)       83.7428 (1.0)      692.1500 (1.0)       9.1500 (1.0)      2021;15505        1.4234 (1.0)       71665          20
test                  676.0001 (1.04)     13,594.9999 (4.59)     741.8349 (1.06)     273.9084 (3.27)     720.9997 (1.04)     26.9997 (2.95)      1546;8491        1.3480 (0.95)     139237           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 3.11 seconds ========
'''''''''''
