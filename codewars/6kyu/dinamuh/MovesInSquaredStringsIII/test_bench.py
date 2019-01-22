from main import rot_90_clock
from main import oper
from main import rot_90_clock2
from main import oper2

def test(benchmark):
    assert benchmark(oper,rot_90_clock, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb")=="Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle"



def test2(benchmark):
    assert benchmark(oper2,rot_90_clock2, "rgavce\nvGcEKl\ndChZVW\nxNWgXR\niJBYDO\nSdmEKb")=="Sixdvr\ndJNCGg\nmBWhca\nEYgZEv\nKDXVKc\nbORWle"






'''''''''''
----------------------------------------------------------------------------------- benchmark: 2 tests -----------------------------------------------------------------------------------
Name (time in us)         Min                Max               Mean            StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test2                  9.3210 (1.0)      88.8050 (1.05)     10.3948 (1.0)      2.9677 (1.0)       9.7370 (1.0)      0.2110 (1.0)     2029;2330       96.2020 (1.0)       34356           1
test                  24.3320 (2.61)     84.9110 (1.0)      25.8346 (2.49)     3.6444 (1.23)     25.0580 (2.57)     0.3300 (1.56)      653;798       38.7079 (0.40)      12773           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.70 seconds ==================================
'''''''''