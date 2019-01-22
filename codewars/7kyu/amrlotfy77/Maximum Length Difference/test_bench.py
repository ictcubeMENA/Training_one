from main import mxdiflg


def test1(benchmark):
    assert benchmark(mxdiflg,
                     ("hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii",
                      "dvvvwz"), ("cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww")) == 13


def test(benchmark):
    assert benchmark(mxdiflg,
                     ("hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii",
                      "dvvvwz"), ("cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww")) == 13
