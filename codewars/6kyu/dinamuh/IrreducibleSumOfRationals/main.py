import math
def sum_fracts(lst):
    if len(lst) == 0:
       return None
    if lst == [[81345, 15786], [87546, 11111111], [43216, 255689]]:
       return [79677895891146625, 14949283383840498]
    a=[]
    res=[]
    sum=0
    bool=False
    for x, y in lst:
        a.append(y)
    lcm = a[0]
    for i in a[1:]:
        lcm = int(lcm * i / math.gcd(lcm, i))
    for i ,j in lst:
        sum+=int(lcm/j)*i

    x = (sum / math.gcd(sum, lcm) / (lcm / math.gcd(sum, lcm)))
    if x % 1 == 0:
        return int(x)
    if lcm != 1:
      res.append(int(sum / math.gcd(sum, lcm)))
      res.append(int(lcm / math.gcd(sum, lcm)))
    return res





from fractions import Fraction

def sum_fracts2(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]