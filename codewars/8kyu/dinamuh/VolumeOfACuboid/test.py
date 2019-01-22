import unittest
from main import getVolumeOfCubiod



def test_getVolumeOfCubiod(benchmark):
        assert benchmark(getVolumeOfCubiod,1, 2, 2)== 4
        assert benchmark(getVolumeOfCubiod,6.3, 2, 5)== 63

