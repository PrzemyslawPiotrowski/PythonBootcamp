import pytest
from mathematica.algebra import metrices

x= [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
result_add = [[17, 15, 4],
              [10, 12, 9],
              [11, 13, 18]]

result_sub = [[7, -1, 2],
              [-2, -2, 3],
              [3, 3, 0]]


def test2():
    assert (metrices.add_metrices(x, y) == result_add)
    assert (metrices.sub_metrices(x, y) == result_sub)
