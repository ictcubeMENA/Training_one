def gps(s, x):
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

def gpsB(s, x):
    if len(x) < 2:
        return 0
    a = max(x[i] - x[i-1] for i in range(1, len(x))) 
    return a * 3600.0 / s
   
        