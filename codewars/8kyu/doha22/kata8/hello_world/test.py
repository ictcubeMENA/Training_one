import unittest
from hello_world import greet

def test_getVolumeOfCubiod(benchmark):
    assert benchmark(greet, ) == "hello world!"
    assert benchmark(greet, ) == "hello world!"
