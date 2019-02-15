def litres(time):
 L = time * 0.5

 L = L - L % 1
    
 return L


def litres1(time):
 return int(time / 2)