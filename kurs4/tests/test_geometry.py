import pytest
from mathematica.geometry import figures

def test1():
    assert (figures.square_area(5) == 25)
    assert (figures.triangle_area(5, 8) == 20)
