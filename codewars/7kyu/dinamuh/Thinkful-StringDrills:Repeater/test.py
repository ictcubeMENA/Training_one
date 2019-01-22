import unittest
from main import repeater



def test_repeater(benchmark):
    assert benchmark(repeater,'a', 5)== 'aaaaa'
    assert benchmark(repeater,'Na', 16)== 'NaNaNaNaNaNaNaNaNaNaNaNaNaNaNaNa'
    assert benchmark(repeater,'Wub ', 6)== 'Wub Wub Wub Wub Wub Wub '
