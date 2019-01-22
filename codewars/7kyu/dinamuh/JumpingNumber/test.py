from main import jumping_number


def test_jumping_number(benchmark):
    assert benchmark(jumping_number, 1) == "Jumping!!"
    assert benchmark(jumping_number, 7) == "Jumping!!"
    assert benchmark(jumping_number, 9) == "Jumping!!"
    assert benchmark(jumping_number, 23) == "Jumping!!"
    assert benchmark(jumping_number, 32) == "Jumping!!"
    assert benchmark(jumping_number, 79) == "Not!!"
    assert benchmark(jumping_number, 98) == "Jumping!!"
    assert benchmark(jumping_number, 8987) == "Jumping!!"
    assert benchmark(jumping_number, 4343456) == "Jumping!!"
    assert benchmark(jumping_number, 98789876) == "Jumping!!"
