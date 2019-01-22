def capitalize(s):
    output11 = ""
    output2 = ""
    c = []

    for x in range(0, len(s)):

        if (x % 2 == 0):
            output11 += s[x].upper()
        else:
            output11 += s[x].lower()

        if (x % 2 == 1):
            output2 += s[x].upper()
        else:
            output2 += s[x].lower()

    c.append(output11)
    c.append(output2)

    return c


def capitalize1(s):
    s = ''.join(c if i % 2 else c.upper() for i, c in enumerate(s))
    return [s, s.swapcase()]
