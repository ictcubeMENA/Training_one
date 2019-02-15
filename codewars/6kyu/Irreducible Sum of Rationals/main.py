from fractions import Fraction

def sum_fracts(lst):
    res = 0
    for i in lst:
        res =res + Fraction(i[0],i[1])
    if res.numerator == 0:
        return None
    if res.denominator != 1:   
        return [res.numerator, res.denominator]     
    else:
        return res.numerator

def sum_fractsB(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]