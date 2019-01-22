def vert_mirror(strng):
    arr = strng.split("\n")
    res = []
    for word in arr:
        w = word[::-1]
        res.append(w)
    return '\n'.join(res)


def hor_mirror(strng):
    # arr = splint("\n")
    arr = strng.split("\n")
    # revirse every element in arr
    res = arr[::-1]
    # return join arr ("\n")
    return '\n'.join(res)


def oper(fct, s):
    return fct(s)


def vert_mirror2(s):
    return "\n".join(line[::-1] for line in s.split("\n"))


def hor_mirror2(s):
    return "\n".join(s.split("\n")[::-1])


def oper2(fct, s):
    return fct(s)
