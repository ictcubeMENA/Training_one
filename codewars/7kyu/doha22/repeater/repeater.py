def repeater(string, n):
    return string*n

def repeater2(string, n):
    return string * n
    
'''''''''
----------------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------
--------------------
Name (time in ns)          Min                       Max                  Mean                 StdDev                Median                   IQR            Outliers  OPS (Kops/s)
  Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------
test2                 410.5287 (1.0)      8,504,513.5583 (3.08)     2,167.2654 (1.34)     29,909.3248 (4.21)     1,642.1150 (1.33)       410.5287 (1.0)      339;8109      461.4110 (0.75)
  152243           1
test                  821.0575 (2.00)     2,761,626.8926 (1.0)      1,623.1283 (1.0)       7,106.2664 (1.0)      1,231.5862 (1.0)      1,231.5862 (3.00)     413;1480      616.0942 (1.0)
  173992           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 2 passed in 8.13 seconds =================================================================================

'''''''''