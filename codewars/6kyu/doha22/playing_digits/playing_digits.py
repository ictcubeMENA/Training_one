def dig_pow(n, p):
    number = str(n)
    t = sum([int(number[i]) ** (p + i) for i in range(len(number))])
    if (t % n) == 0 :
        return round (t / n ) 
    else: 
        return -1
    

def dig_pow2(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
