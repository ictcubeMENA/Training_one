def square_digits(num):
    s = str(num)
    res = ''
    for d in s:
        x = int(d) ** 2
        res += str(x)
    return int(res)

    return square_digits(9119)


def square_digits1(num):
    ret = ""
    for x in str(num):
        ret += str(int(x) ** 2)
    return int(ret)
