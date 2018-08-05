import json

pytanie = "Co chcesz zrobic? [d-dodaj] [w-wypisz] [k-koniec]"
pytanie2 = ('Imie', 'Nazwisko','Rok Urodzenia', 'Pensja')
lista = {}
licznik = 0

while True:
    x = input(pytanie)
    if x == "d":
        licznik += 1
        lista[licznik] = {}
        for x in pytanie2:
            lista[licznik].update({x:input(x)})
    with open("pracownicy.json", 'w') as f:
        json.dump(lista, f)
    if x == "w":
        with open("pracownicy.json", encoding='utf8') as f:
            print(json.load(f))
    if x == "k":
        break
