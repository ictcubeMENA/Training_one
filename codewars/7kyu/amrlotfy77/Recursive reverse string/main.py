def reverse(str):
    if (len(str) == 1):
        return str
    else:
        return reverse(str[1:]) + str[0]


def reverse1(str):
    return ''.join(reversed(str))
