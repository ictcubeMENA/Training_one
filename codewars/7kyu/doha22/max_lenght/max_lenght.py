def mxdiflg(a1, a2):
    if a1 and a2: 
        res1 = max([len(x) for x in a1])
        res11 = min([len(x) for x in a1])
        res2 = max([len(x) for x in a2])
        res22 = min([len(x) for x in a2])
        return max(res1 - res22, res2 - res11)
    else:
        return -1 
#print(mxdiflg(["hoqq", "bbllkw", "oox"],["cccooommaaqqoxii", "gggqaffhhh"]))
def mxdiflg2(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1