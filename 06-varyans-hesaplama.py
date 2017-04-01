"""
varyans'i bulmak icin listenin ortalamasi bulunur.
her elemanin ortalama ile farkinin karesi alinir ve toplam degiskenine atanir.
bu toplami eleman sayisina bolersek varyans'i elde etmis oluruz.
"""

def varyans_hesap(liste,sayi,ort):
    toplam = 0
    for i in range(0,sayi):
        toplam += (ort - liste[i])**2

    print("Listenin Varyansı ==> {}".format(toplam / sayi))


sayi = int(input("Listeye Kac Sayi Gireceksin ? : "))
liste = []

for i in range(0,sayi):
    liste.append(int(input("{}. sayiyi gir : ".format(i+1))))

toplam = sum(liste)
ortalama = toplam / sayi
varyans_hesap(liste,sayi,ortalama)
