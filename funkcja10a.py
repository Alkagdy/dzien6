def dodaj_imie(imie, imiona=None):
    if imiona is None:
        imiona = []
    imiona.append(imie)
    return imiona

lista1 = dodaj_imie("Ala")
lista2 = dodaj_imie("Ola")
print(lista1)
print(lista2)





