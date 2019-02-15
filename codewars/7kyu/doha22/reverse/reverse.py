def reverse(a):
    s=reversed(''.join(a))
    return [''.join(next(s) for _ in w) for w in a]

def reverse2(a):
    s = ''.join(a)[::-1]
    l, x = [], 0
    for i in a:
        l.append(s[x:x+len(i)])
        x += len(i)
    return l


