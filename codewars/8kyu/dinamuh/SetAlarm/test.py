import unittest
from main import set_alarm



def test_set_alarm(benchmark):
    assert benchmark(set_alarm,True, True)== False, "Fails when input is True, True"
    assert benchmark(set_alarm,False, True)== False, "Fails when input is False, True"
    assert benchmark(set_alarm,False, False)== False, "Fails when input is False, False"
    assert benchmark(set_alarm,True, False)== True, "Fails when input is True, False"
