from main import camel_case,camel_case1


def test1(benchmark):
      assert benchmark(camel_case,"test case")== "TestCase"


def test(benchmark):
    assert benchmark(camel_case1, "test case") == "TestCase"