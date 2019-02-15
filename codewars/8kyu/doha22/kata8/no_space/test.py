import unittest
from no_space import no_space

def test_no_space(benchmark):
    assert benchmark(no_space, '8 j 8   mBliB8g  imjB8B8  jl  B') == '8j8mBliB8gimjB8B8jlB'
    assert benchmark(no_space,'8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd' ) == '88Bifk8hB8BB8BBBB888chl8BhBfd'
