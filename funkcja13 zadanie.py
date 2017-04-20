#funkcja sprawdzajaca czy podany string jest palindromem
#wykorzystanie funkcji z innego pliku

#import funkcja7

#funkcja7.odwrocony_str()

def odwrocony_str(zdanie):
    return zdanie[::-1]

odwrocony = odwrocony_str("Ala ma kota")

print(odwrocony)

def czy_palindrom(fraza):
    """Sprawdza czy fraza jest palindromem"""
    odwrocony = odwrocony_str(fraza)
    for litera1, litera2 in zip(fraza, odwrocony):
        if litera1 != litera2:
            return False
        return True


print(czy_palindrom("Ala"))

