def mxdiflg(a1, a2):
    allmax = []
    counter = 0
    if len(a1) and len(a2) != 0:
        if len(a1) > len(a2):
            while counter <= len(a1):
                for x in a1:
                    for y in a2:
                        allmax.append(abs(len(x) - len(y)))
                        counter += 1
            return max(allmax)
        if len(a1) <= len(a2):
            while counter <= len(a2):
                for x in a1:
                    for y in a2:
                        allmax.append(abs(len(x) - len(y)))
                        counter += 1
            return max(allmax)
    if not a1 or not a2:
        return (-1)


def mxdiflg1(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1
