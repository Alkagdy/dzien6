#mozemy miec kilka argumentow wymaganych i domyslnych
#dwa pierwsze sa wymagane, a dwa ostatnie domyslne

def wypisz_dane(imie, nazwisko, kurs ="Python", ilosc_dni=15):
    print(imie, nazwisko, kurs, ilosc_dni)

wypisz_dane("arek", "g")
wypisz_dane("Ala", "gajda", ilosc_dni=45)

