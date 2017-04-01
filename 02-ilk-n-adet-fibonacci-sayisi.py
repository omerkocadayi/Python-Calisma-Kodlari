# ILK N ADET FIBONACCI SAYISINI YAZDIRMA

sayi = int(input('Bir sayi giriniz : '))
print("Fibonacci sayi dizisinin ilk {} sayisi" .format(sayi))

a, b = 1, 1
print (a)
print (b)

for i in range(2,sayi):
    a, b = b, a+b
    print (b)
    i += 1
