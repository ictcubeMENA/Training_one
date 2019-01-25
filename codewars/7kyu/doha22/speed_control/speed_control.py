def gps(s, x):
    # your code
    rs = []
    sp = 0
    if len(x) <= 1:
        return 0
    else:
        for i in range (len(x)-1):
            xx =x[i+1]- x[i]
            rs.append((3600 * xx) / s)
            sp = int((max(rs)))
        return sp
        
def gps2(s, x):
    if len(x) < 2:
        return 0
    dist = []
    speed = []
    i = 0
    while i < (len(x) - 1):
        dist.append(x[i+1] - x[i])
        i += 1
    for n in dist:
        speed.append(int((3600 * n) / s))
    return max(speed)

