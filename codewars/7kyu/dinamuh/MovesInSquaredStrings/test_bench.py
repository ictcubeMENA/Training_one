from main import vert_mirror
from main import hor_mirror
from main import oper
from main import vert_mirror2
from main import hor_mirror2
from main import oper2

def test(benchmark):
    assert benchmark(oper, vert_mirror,
                     "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu") == "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"


def test2(benchmark):
    assert benchmark(oper2, vert_mirror2,
                     "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu") == "QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw"









'''''''''
---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
Name (time in us)        Min                Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test                  1.5000 (1.0)      14.4330 (1.0)      1.6243 (1.0)      0.4013 (1.0)      1.5860 (1.0)      0.0520 (1.0)      1734;5602      615.6448 (1.0)      109314           1
test2                 1.5800 (1.05)     28.3360 (1.96)     1.7621 (1.08)     0.5048 (1.26)     1.7000 (1.07)     0.0650 (1.25)     2275;7741      567.4974 (0.92)     125016           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
============================================================================ 2 passed in 2.49 seconds ==============================
'''''''''