import pytest

def czy_palindrom(napis):
    if napis == napis[::-1]:
        print(True)
        return True
    else:
        print(False)
        return False


czy_palindrom('kajak')
czy_palindrom('python')

@pytest.mark.parametrize(
    'tekst, word', [
        ('kajak', True),
        ('python', False)
    ])
def test_czy_palindrom(tekst, word):
    assert czy_palindrom(tekst) == word
