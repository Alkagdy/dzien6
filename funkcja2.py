#definiowanie z argumentami

def drukuj_kwadraty():
    liczby = range(12)
    for l in liczby:
        print(l **2)

drukuj_kwadraty()

#max_num zmienna lokalna
def drukuj_kwadraty1(max_num):
    for l in range(max_num):
        print(l**2)

drukuj_kwadraty1(10)