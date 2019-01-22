def scale(strng, k, n):
    if strng == "":
        return ""
    res = ""
    s1 = strng.split("\n")
    for i in range(len(s1)):
        s = ""
        for y in range(len(s1[i])):
            for j in range(k):
                s += s1[i][y]
        for p in range(n):
            res += s + "\n"
    return res[0:len(res) - 1]


def scale_horizontal(strng, k):
    retstrng = strng
    if k > 1:
        s = [s * k for s in strng]
        retstrng = "".join(s)
    return retstrng


def scale1(strng, k, n):
    if strng == "": return ""
    lines = strng.split('\n')
    lines = [scale_horizontal(line, k) for line in lines]
    retlines = []
    for i in range(len(lines)):
        for j in range(n):
            retlines.append(lines[i])
    return "\n".join(retlines)

# ---------------------------------------------------------------------------------- benchmark: 2 tests ----------------------------------------------------------------------------------
# Name (time in us)        Min                Max              Mean            StdDev            Median               IQR             Outliers  OPS (Kops/s)            Rounds  Iterations
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# scale1                  2.8610 (1.0)      27.8950 (1.0)      4.2310 (1.0)      1.6338 (1.0)      4.0531 (1.0)      0.0000 (1.0)      864;22879      236.3490 (1.0)       66577           1
# scale                 4.7684 (1.67)     57.9357 (2.08)     6.4022 (1.51)     2.1830 (1.34)     5.9605 (1.47)     0.2384 (inf)     2607;10939      156.1975 (0.66)      67651           1
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
