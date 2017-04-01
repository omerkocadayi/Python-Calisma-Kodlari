def tersi(sayi, toplam):
    if sayi == 0:
        return toplam

    gecici = sayi%10
    toplam = (toplam*10) + gecici
    return tersi(sayi//10,toplam)

toplam = 0
sayi = int(input("sayini gir : "))
print("ters hali = {}".format(tersi(sayi, toplam)))