#funkcja zwracajaca odwrocony string

def odwrocony_str(zdanie):
    return zdanie[::-1]

odwrocony = odwrocony_str("Ala ma kota")

print(odwrocony)
print(odwrocony_str("Stol z powylamywanymi nogami"))

def odwroc_input():
    zdanie = input("Podaj zdanie:")
    return zdanie[::-1]

print(odwroc_input())
