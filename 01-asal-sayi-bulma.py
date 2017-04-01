# ASAL SAYI BULMA

sayi = int(input('Bir sayi giriniz : '))
bolundu = 0
for i in range(2, (sayi+1)//2):
    if sayi%i == 0:
        print ("Girdiginiz sayi asal degildir !!")
        bolundu += 1
        break

if (bolundu == 0):
    print ("Bu sayi asaldir !!")
