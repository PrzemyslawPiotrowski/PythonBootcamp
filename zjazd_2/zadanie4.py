import pytest

def policz_slowa(tekst):
    skladzik = {}
    for x in set(tekst.split(' ')):
        skladzik.update({x:tekst.count(x)})
    print(skladzik)
    return skladzik



policz_slowa('ala ma kota i kota ma ala')


def test_policz_slowa():
    assert policz_slowa('ala ma kota i kota ma ala') == {'kota': 2, 'ma': 2, 'ala': 2, 'i': 1}
