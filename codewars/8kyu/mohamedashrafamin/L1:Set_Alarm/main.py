def set_alarm(employed, vacation):
    return employed and not vacation


def set_alarm1(employed, vacation):
    return employed and not vacation

# -------------------------------------------------------------------------------------- benchmark: 2 tests --------------------------------------------------------------------------------------
# Name (time in ns)         Min                   Max                Mean             StdDev             Median               IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# test1                 78.6781 (1.0)      1,800.0603 (2.78)     103.1582 (1.08)     44.1888 (1.73)     90.5991 (1.0)      9.5367 (inf)      5773;6167        9.6939 (0.93)      99865         100
# test                  88.2149 (1.12)       648.4985 (1.0)       95.7671 (1.0)      25.4842 (1.0)      90.5991 (1.0)      0.0000 (1.0)      827;15217       10.4420 (1.0)       35849         100
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
