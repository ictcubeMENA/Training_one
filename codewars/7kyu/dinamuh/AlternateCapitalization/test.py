import unittest
from main import capitalize



def test_capitalize(benchmark):
        assert benchmark(capitalize,"abcdef")==['AbCdEf', 'aBcDeF']
        assert benchmark(capitalize,"codewars")==['CoDeWaRs', 'cOdEwArS']
        assert benchmark(capitalize,"abracadabra")==['AbRaCaDaBrA', 'aBrAcAdAbRa']
        assert benchmark(capitalize,"codewarriors")==['CoDeWaRrIoRs', 'cOdEwArRiOrS']

