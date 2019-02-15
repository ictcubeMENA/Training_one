def find_short(s):
    w = s.split(' ')
    w.sort(key=len)
    x = len(w[0])
    return x


def find_short1(s):
    return len(min(s.split(' '), key=len))
