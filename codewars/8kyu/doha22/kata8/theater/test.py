import unittest
from main import seats_in_theater


def test_seats_in_theater(benchmark):
	assert benchmark(seats_in_theater(16,11,5,3)) == 96 	
    	assert benchmark(seats_in_theater(1,1,1,1)) == 0
