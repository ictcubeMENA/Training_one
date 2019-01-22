from main import scale, scale1

a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"


def test1(benchmark):
    assert benchmark(scale, a, 2, 3) == r


def test(benchmark):
    assert benchmark(scale1, a, 2, 3) == r

# py.test
