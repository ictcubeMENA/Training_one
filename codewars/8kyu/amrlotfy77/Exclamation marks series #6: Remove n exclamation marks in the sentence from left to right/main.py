def remove(s, n):
    l = []
    for i in s:
        if i == "!" and n > 0:
            n -= 1
            continue
        l.append(i)
    return ''.join(l)


def remove1(s, n):
    q=s.replace('!','',n)
    return q