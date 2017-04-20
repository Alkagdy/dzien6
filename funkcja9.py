#zmienna na poziomie globalnym
imie = "jola"

def drukuj_imiona(imie_2):
    global imie #global powoduje, ze glowna zmienna jest imie="ania"
    imie = "ania"
    imie = imie.capitalize()
    imie_2 = str(imie_2.capitalize())

    print(imie, imie_2)

drukuj_imiona("gosia")
print(imie)



