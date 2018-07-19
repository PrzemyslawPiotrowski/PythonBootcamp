import pytest

def lata_przestepne(poczatek,koniec):
    skladzik = [x for x in range(poczatek,koniec + 1) if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)]
    print(skladzik)
    return skladzik

lata_przestepne(1990,2020)


def test_lata_przestepne():
    assert lata_przestepne(1990,2020) == [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
