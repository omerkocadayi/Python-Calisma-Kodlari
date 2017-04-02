def convert_binary(sayi):
    liste = []

    while True:
        liste.insert(0,sayi%2)
        sayi = sayi // 2

        if sayi<2:
            liste.insert(0,sayi)
            break

    print(liste)

sayi = int(input("Sayini gir : "))
