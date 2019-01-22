from main import oper
from main import oper2
from main import rot
from main import rot2


def test(benchmark):
    assert benchmark(oper, rot,
                     "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL") == "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif"


def test2(benchmark):
    assert benchmark(oper2, rot2,
                     "fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL") == "LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif"


''''''''''

---------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
Name (time in ns)          Min                   Max                Mean             StdDev              Median               IQR              Outliers  OPS (Mops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 246.1000 (1.0)      2,636.4500 (1.41)     258.4908 (1.0)      36.4302 (1.0)      254.2501 (1.0)      3.7499 (1.0)      3126;13063        3.8686 (1.0)      192456          20
test                  247.1999 (1.00)     1,865.9500 (1.0)      261.7058 (1.01)     41.9961 (1.15)     256.5500 (1.01)     4.1000 (1.09)      2464;9185        3.8211 (0.99)     157209          20
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 4.47 seconds =============================================================================
'''''''''''
