ogrenciler = []
sorular = ["ad", "soyad", "yas", "is"]

def goster():
    print(*[soru.upper() for soru in sorular])

    for ogrenci in ogrenciler:
        print(*[ogrenci[soru] for soru in sorular])


def ekle():
    ogrenci = {}

    for soru in sorular:
        cevap = input(soru.capitalize() + ": ")
        ogrenci[soru] = cevap

    return ogrenci


while True:
    girdi = input("Sıralamak için S, Eklemek için E yazın, Çıkmak için Q yazın\n>>>")
    girdi = girdi.lower()

    if girdi == "s":
        goster()

    elif girdi == "e":
        ogr = ekle()
        ogrenciler.append(ogr)

    elif girdi == "q":
        quit()  # exit()  # break

    elif girdi == "":
        pass

    else:
        print("Hatalı Giriş")