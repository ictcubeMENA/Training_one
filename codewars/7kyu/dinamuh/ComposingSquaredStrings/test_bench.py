from main import compose
from main import compose2


def test(benchmark):
    assert benchmark(compose, "byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB") == "bNkTB\nhTrWO\nRTFVi\nCnnIj"


def test2(benchmark):
    assert benchmark(compose2, "byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB") == "bNkTB\nhTrWO\nRTFVi\nCnnIj"


'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  2.0860 (1.0)      17.8420 (1.02)     2.2163 (1.0)      0.4959 (1.0)      2.1630 (1.0)      0.0690 (1.06)     1567;4047      451.2056 (1.0)       80613           1
test2                 2.0980 (1.01)     17.5290 (1.0)      2.2267 (1.00)     0.5060 (1.02)     2.1750 (1.01)     0.0650 (1.0)      2315;5965      449.0881 (1.00)     150716           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.58 seconds =========
'''''
