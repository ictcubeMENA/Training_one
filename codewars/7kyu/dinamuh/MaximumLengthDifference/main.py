def mxdiflg(a1, a2):
    if len(a1) < 1 or len(a2) < 1:
        return -1

    max1 = 0
    min1 = len(a1[0])
    for m1 in a1:
        l = len(m1)
        if l > max1:
            max1 = l
        if l < min1:
            min1 = l
    max2 = 0
    min2 = len(a2[0])
    for m2 in a2:
        l = len(m2)
        if l > max2:
            max2 = l
        if l < min2:
            min2 = l

    diff1 = max1 - min2
    diff2 = max2 - min1
    return max(diff1, diff2)


def mxdiflg2(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1
