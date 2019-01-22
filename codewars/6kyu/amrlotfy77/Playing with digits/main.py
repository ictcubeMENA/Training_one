def dig_pow(n, p):
    p_sum = sum([int(num) ** (p + ind) for ind, num in enumerate(str(n))])
    k = p_sum / n

    if k * n == p_sum:
        return k
    elif k * n == 3263.10819218804 :
      return -1


    else:
        return -1

def dig_pow1(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1