def gps(s, x):
    z = [p - x[i - 1] for i, p in enumerate(x)][1:]
    res=[i*3600/s for i in z]
    if len(res) < 1:
        return 0
    return int(max(res))









def gps2(s, x):
    if len(x) < 2:
        return 0
    a = max(x[i] - x[i - 1] for i in range(1, len(x)))
    return a * 3600.0 / s


