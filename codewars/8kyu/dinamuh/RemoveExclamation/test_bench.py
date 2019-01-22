from main import remove_exclamation_marks
from main import remove_exclamation_marks2

def test(benchmark):
    assert benchmark(remove_exclamation_marks, "Hello World!") == "Hello World"


def test2(benchmark):
    assert benchmark(remove_exclamation_marks2, "Hello World!") == "Hello World"




'''''''''
---------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
Name (time in ns)          Min                   Max                Mean             StdDev              Median               IQR              Outliers  OPS (Mops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 235.9000 (1.0)      2,425.6000 (1.41)     249.9238 (1.0)      44.5728 (1.0)      243.0000 (1.0)      3.7500 (1.0)      4356;24006        4.0012 (1.0)      199283          20
test                  244.6500 (1.04)     1,718.5000 (1.0)      272.1774 (1.09)     51.7308 (1.16)     265.3500 (1.09)     4.4500 (1.19)     3961;34800        3.6741 (0.92)     183756          20
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 4.95 seconds ==================================================================
'''''''''''