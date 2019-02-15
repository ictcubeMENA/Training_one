from main import set_alarm


def test(benchmark):
    assert benchmark(set_alarm, False, True) == False, "Fails when input is False, True"


def test2(benchmark):
    assert benchmark(set_alarm, False, True) == False, "Fails when input is False, True"


''''''''''
------------------------------------------------------------------------------------- benchmark: 2 tests -------------------------------------------------------------------------------------
Name (time in ns)         Min                 Max                Mean             StdDev             Median               IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                 95.9300 (1.0)      469.3200 (1.0)      101.6314 (1.01)     15.5180 (1.05)     98.0750 (1.0)      0.8200 (1.30)    2139;19494        9.8395 (0.99)      99030         100
test                  96.0800 (1.00)     474.1600 (1.01)     100.6860 (1.0)      14.8287 (1.0)      98.1400 (1.00)     0.6300 (1.0)      3660;7783        9.9319 (1.0)       94376         100
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 3.93 seconds =================
'''''''''''''''''
