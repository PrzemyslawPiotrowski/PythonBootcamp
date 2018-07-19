import pytest

def filtruj(lista, zakres1, zakres2):
    skladzik = []
    for x in lista:
        if x in range(zakres1, zakres2+1):
            skladzik.append(x)
    print(skladzik)
    return skladzik

filtruj([-2, 10, 0, 5, 1, 16, 9], 5, 15)


def test_filtruj():
    assert filtruj([-2, 10, 0, 5, 1, 16, 9], 5, 15) == [10, 5, 9]
