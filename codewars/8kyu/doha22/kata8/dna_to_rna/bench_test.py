from dna_to_rna import DNAtoRNA
from dna_to_rna import DNAtoRNA2

def test(benchmark):
    assert benchmark(DNAtoRNA,"TTTT") == "UUUU"



def test2(benchmark):
    assert benchmark(DNAtoRNA2, "TTTT") == "UUUU"

'''''''''
------------------------------------------------------------------------------------ benchmark: 2 tests -----------------------------------------------------------------------------------
Name (time in us)        Min                   Max              Mean             StdDev            Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.6421 (1.0)      2,021.0305 (2.27)     2.9110 (1.0)      10.4601 (1.73)     2.0526 (1.0)      1.2316 (3.00)     370;1661      343.5240 (1.0)       73815           1
test2                 3.6948 (2.25)       890.8463 (1.0)      4.6689 (1.60)      6.0396 (1.0)      4.1053 (2.00)     0.4105 (1.0)      695;9561      214.1833 (0.62)      65835           1
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 7.18 seconds =================================================================================

'''''''''