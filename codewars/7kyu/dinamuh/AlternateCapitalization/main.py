def capitalize(s):
    ##
    p = ''
    ev = ''
    index = 0
    for i in s:
        if index % 2 == 0:
            ev += s[index].upper()
        else:
            ev += s[index]
        index += 1
    index = 0
    for i in s:
        if index % 2 == 1:
            p += s[index].upper()
        else:
            p += s[index]
        index += 1

    return [ev, p]



def capitalize2(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]