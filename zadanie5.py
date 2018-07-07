pytanie = ("""dostepne produkty, co chesz kupic?
    K - kielbasa
    M - makaron
    R - ryz
    Z - ziemniaki
    KONIEC - koniec zakupow""")
pytanie2 = ("Ile Kg??")

cena = {'K': 22.50, 'M': 2.10, 'R': 1, 'Z': 2.22}

wynik = 0
while True:
    x = input(pytanie)
    if x != "KONIEC":
        while x in cena.keys():
            y = float(input(pytanie2))
            wynik = wynik + cena[x] * y
            break
        else:
            print('nie ma takiego produktu sprobuj jeszcze raz')
    else:
        break
print(f'do zaplaty {wynik}')
