def find_short(s):
    # your code here
    m = min(s.split(), key = len)
    l = len(m)
    return l

def find_short2(s):
    return min(len(x) for x in s.split())