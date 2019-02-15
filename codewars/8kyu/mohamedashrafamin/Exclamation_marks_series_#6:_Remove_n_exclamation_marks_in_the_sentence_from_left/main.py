def remove(s, n):
    return s.replace("!", "", n)


def remove1(s, n):
    return s.replace("!", "", n)

# --------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
# Name (time in ns)          Min                   Max                Mean             StdDev              Median               IQR             Outliers  OPS (Mops/s)            Rounds  Iterations
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# remove1               188.3507 (1.0)      2,801.4183 (3.30)     205.6669 (1.0)      50.2309 (1.30)     200.2716 (1.0)      9.5367 (1.0)      1975;2208        4.8622 (1.0)       49933         100
# remove                 188.3507 (1.0)        848.7701 (1.0)      205.9715 (1.00)     38.5556 (1.0)      200.2716 (1.0)      9.5367 (1.0)      1501;2113        4.8550 (1.00)      43691         100
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
