def kelime_sayisi(string):
    counter = 1
    for i in range(0,len(string)):
        if string[i] == ' ':
            counter += 1

    return counter

cumle = input("Cumlenizi giriniz : ")
print("Cumlenizdeki kelime sayisi = {}".format(kelime_sayisi(cumle)))
