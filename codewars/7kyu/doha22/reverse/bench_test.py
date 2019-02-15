from reverse import reverse
from reverse import reverse2


def test(benchmark):
    assert benchmark(reverse, ["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"]) ==["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts", "to", "turn", "pink?"]

def test2(benchmark):
    assert benchmark(reverse2, ["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"]) == ["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts", "to", "turn", "pink?"]

'''''''''''
--------------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
----
Name (time in us)         Min                   Max                Mean             StdDev              Median                IQR            Outliers  OPS (Kops/s)            Rounds  Iterat
ions
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----
test2                 19.2949 (1.0)      1,477.9035 (1.81)      35.2222 (1.0)      20.0098 (1.0)       35.3055 (1.0)      17.6527 (1.0)       474;318       28.3912 (1.0)       15921
   1
test                  74.3057 (3.85)       818.5943 (1.0)      121.7485 (3.46)     52.7606 (2.64)     127.0586 (3.60)     75.1268 (4.26)       220;47        8.2137 (0.29)       2826
   1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
----

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 3.03 seconds =================================================================================

'''''