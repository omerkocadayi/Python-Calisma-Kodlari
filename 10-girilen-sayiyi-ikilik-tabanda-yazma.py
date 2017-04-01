def convert_binary(sayi):
    liste = []
    i = 0

    while True:
        liste.insert(i,sayi%2)
        sayi = sayi // 2

        if sayi<2:
            liste.insert(0,sayi)
            break
        i += 1

    print(liste)

sayi = int(input("Sayini gir : "))
print("\nSayinin ikilik taban karsiligi\n{}".format(convert_binary(sayi)))