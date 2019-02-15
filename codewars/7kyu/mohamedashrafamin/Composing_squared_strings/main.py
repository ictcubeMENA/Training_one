def compose(s1, s2):
    st = s1.split("\n")
    st1 = s2.split("\n")
    res = ""
    s = ""
    for i in range(len(st[1])):
        s += st[i][0:i + 1]
        res += s + (st1[len(st1) - (i + 1)][0:len(st1[len(st1[0]) - (i + 1)]) - i]) + "\n"
        s = ""
    return res[0:len(res) - 1]


def compose1(s1, s2):
    s1 = s1.split("\n")
    s2 = s2.split("\n")[::-1]

    n = len(s1)
    out = []

    for i in range(n):
        out.append(s1[i][:i + 1] + s2[i][:(n - i)])

    return "\n".join(out)

# ---------------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------------
# Name (time in ns)            Min                     Max                  Mean                StdDev                Median                 IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# compose                  953.6743 (1.0)      204,086.3037 (2.20)     1,967.4656 (1.39)     1,575.7744 (2.62)     1,907.3486 (1.47)     238.4186 (1.75)    2722;24906      508.2681 (0.72)      89241           1
# compose1                  1,123.9733 (1.18)      92,847.0067 (1.0)      1,420.1835 (1.0)        600.5647 (1.0)      1,294.2723 (1.0)      136.2392 (1.0)      4745;6422      704.1343 (1.0)       99865           7
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
