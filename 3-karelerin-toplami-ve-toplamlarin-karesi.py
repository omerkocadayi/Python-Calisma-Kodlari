# Birden yüze kadar sayıların karelerinin toplamı ile toplamlarının karelerinin farkı

toplam, karetoplami=0,0

for i in range(1,101):
    toplam += i
    karetoplami += i**2

print("Farklari = {}".format(toplam**2 - karetoplami))