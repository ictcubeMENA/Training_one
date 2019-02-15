import unittest
from max_lenght import mxdiflg, mxdiflg2

a1 =  ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 =["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
a3 = ["hoqq", "bbllkw", "oox"]
a4= ["cccooommaaqqoxii", "gggqaffhhh"]
def test_mxdiflg(benchmark):
    assert benchmark(mxdiflg,a1,a2) == 13
    assert benchmark(emxdiflg2,a3,a4) == 13
