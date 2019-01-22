import unittest
from main import isLeapYear



def test_isLeapYear(benchmark):
        assert benchmark(isLeapYear,1984)== True, 'Year 1984 was a leap year!'
        assert benchmark(isLeapYear,2000)== True, 'Year 2000 was a leap year!'
        assert benchmark(isLeapYear,1234)== False, 'Year 1234 was NOT a leap year!'
        assert benchmark(isLeapYear,1100)== False, 'Year 1100 was NOT a leap year!'
