def litres(time):
    return int(time / 2)


def litres1(time):
    return time // 2

# ---------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------
# Name (time in ns)          Min                   Max                Mean             StdDev              Median               IQR              Outliers  OPS (Mops/s)            Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# litres1                  97.7516 (1.0)        889.3013 (1.0)      113.6608 (1.0)      30.4916 (1.0)      109.6725 (1.0)      0.0000 (1.0)      2149;35571        8.7981 (1.0)       82242         100
# litres                 169.2772 (1.73)     1,571.1784 (1.77)     201.2724 (1.77)     50.1193 (1.64)     190.7349 (1.74)     2.3842 (inf)      2938;12479        4.9684 (0.56)      49933         100
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
