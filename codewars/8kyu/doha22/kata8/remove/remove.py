def remove(s, n):
    pass
    if("!" in s): 
        x=s.replace("!","",n)
        return x


def remove2(s, n):
    while n > 0:
        s = s.replace('!','',1)
        n -= 1
    return s