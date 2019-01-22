def vert_mirror(strng):
    l1 = strng.split("\n")
    l2 = [x[::-1] for x in l1]
    s2 = "\n".join(l2)
    return s2


def hor_mirror(strng):
    l1 = strng.split("\n")
    l2 = l1[::-1]
    s2 = "\n".join(l2)
    return


def oper(fct, s):
    return fct(s)
