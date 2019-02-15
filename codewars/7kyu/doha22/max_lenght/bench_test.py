from max_lenght import mxdiflg
from max_lenght import mxdiflg2

a1 =  ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 =["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
def test(benchmark):
    assert benchmark(mxdiflg, a1,a2) == 13


def test2(benchmark):
    assert benchmark(mxdiflg2, a1,a2) == 13

''''''''''
--------------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
----
Name (time in us)         Min                    Max               Mean              StdDev             Median                IQR            Outliers  OPS (Kops/s)            Rounds  Iterat
ions
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----
test                  15.6001 (1.0)       4,373.3628 (1.0)      25.2615 (1.0)       33.8366 (1.0)      23.8107 (1.0)      14.7790 (1.64)      285;340       39.5859 (1.0)       19967
   1
test2                 27.9160 (1.79)     13,629.9650 (3.12)     63.5326 (2.51)     203.0582 (6.00)     50.0845 (2.10)      9.0316 (1.0)      126;1836       15.7399 (0.40)      13609
   1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 5.24 seconds =================================================================================

'''''''''''