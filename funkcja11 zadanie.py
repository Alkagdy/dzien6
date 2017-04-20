def czy_w_zakresie(liczba, zakres):
    """Sprawdza czy podana liczba jest w zakresie. Zwraca True jesli jest
    (liczba) -> bool """
    if liczba in zakres:
        return True
    else:
        return False

x = 12
y = range(1, 23)
wynik = czy_w_zakresie(x,y)

print(wynik)

liczby = [23,345,765,4278]

for liczba in liczby:
    print(czy_w_zakresie(liczba, range(100000)))

