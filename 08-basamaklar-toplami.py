bilgi="""
Girilen sayinin basamaklari toplamini
ozyinelemeli bir fonksiyon kullanarak bulunuz.
"""

def basamaklar_toplami(x):
    if(x==0):
        return 0

    else:
        return x%10 + basamaklar_toplami(x//10)

sayi = int(input("\nSayiyi giriniz : "))
print("Sayinin basamaklari toplami = {}".format(basamaklar_toplami(sayi)))
