def array_diff(a, b):
    res = []
    for itemA in a:
        if not itemA in b :
            res.append(itemA)
    return res




def array_diff2(a, b):
    return [x for x in a if x not in b]


