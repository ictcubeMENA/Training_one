def capitalize(s):
    s1 = ''
    s2 = ''
    n = 0
    for char in s:
        if n % 2 != 0:
             s1 += s[n]
             s2 += s[n].upper()
        else:
            s1 += s[n].upper()
            s2 += s[n]
        n += 1
    return [s1,s2]