def seven(m):
    c = 0
    while m >= 100:
        m = m // 10 - 2*(m % 10)
        c += 1
    return (m, c)

def seven2(m):
    steps = 0
    while m > 99:
        q, r = divmod(m, 10)
        m = q - (2 * r)
        steps += 1
    return m, steps