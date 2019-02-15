def scale(strng, h, v):
    # your code
    strin = ""
    if strng == "":
        return ""
    else:
        arr = strng.split("\n")
        resarr = []
        for w in arr:
            a = ""
            for c in w:
                a += c * h
            resarr.append(a)
        finalarr = []
        for w in resarr:
            for i in range(v):
                finalarr.append(w)
    return "\n".join(finalarr)


def scale_horizontal(strng, k):
    retstrng = strng
    if k > 1:
        s = [s * k for s in strng]
        retstrng = "".join(s)
    return retstrng


def scale2(strng, k, n):
    if strng == "": return ""
    lines = strng.split('\n')
    lines = [scale_horizontal(line, k) for line in lines]
    retlines = []
    for i in range(len(lines)):
        for j in range(n):
            retlines.append(lines[i])
    return "\n".join(retlines)
