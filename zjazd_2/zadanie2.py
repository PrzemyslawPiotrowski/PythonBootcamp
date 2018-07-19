import pytest

def filtruj(lista, zakres1, zakres2):
    skladzik = [x for x in lista if x in range(zakres1, zakres2+1)]
    print(skladzik)
    return skladzik

filtruj([-2, 10, 0, 5, 1, 16, 9], 5, 15)


def test_filtruj():
    assert filtruj([-2, 10, 0, 5, 1, 16, 9], 5, 15) == [10, 5, 9]
