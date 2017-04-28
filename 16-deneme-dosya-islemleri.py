f = open("sinavsonuclarim.txt", "w+")
f.write("B dersi : 70\n")
f.write("G dersi : 55\n")
f.write("D dersi : 60\n")
f.write("E dersi : 75\n")
f.write("F dersi : 80\n")

f.seek(0)
print(f.read())

print("Dosyanin kacinci karakteri uzerindeyiz : {}\n\n" .format(f.tell()))
f.seek(0)


# DOSYA BASINA EKLEME YAPMA

veri = f.read()
f.seek(0)
f.write("A dersi : 65\n" + veri)

f.seek(0)

print("Basa ekleme yaptiktan sonra dosya icerigi")
print(f.read())

f.seek(0)



# ARAYA EKLEME YAPMA

data = f.readlines()                    # tum icerigi liste olarak almamiz gerekiyor.
data.insert(2, "C dersi : 85\n")
f.seek(0)
f.writelines(data)                      # tum verileri dosyaya yaziyoruz.


f.seek(0)
print("\nAraya ekleme yaptiktan sonra dosya icerigi")
print(f.read())


# ISTEDIGIMIZ SATIRDAN SONRAKİ VERİLERİ KIRPMA
f.seek(0)
for i in range(1,7):
    f.readline()

a = f.seek(f.tell())
print("\nDosyanin {}inci karakterinden sonraki verileri silinecek" .format(a))
f.truncate(a)


f.seek(0)
print("Silme islemi yaptiktan sonra dosya icerigi")
print(f.read())

f.seek(0)

# ARADAN VERİ SİLME
data = f.readlines()
data.pop(3)
f.truncate(0)
f.writelines(data)

f.seek(0)
print("\nAradan silme islemi yaptiktan sonra dosya icerigi")
print(f.read())


####################


print("\nDosya kapalı mı : {} ".format(f.closed))
print("Dosya okunabilir mi : {} ".format(f.readable()))
print("Dosya yazılabilir mi : {} ".format(f.writable()))
print("Dosya hangi kipte açıldı : {} ".format(f.mode))
print("Dosyanın ismi : {} ".format(f.name))
print("Dosya hangi dil kodlaması ile kodlandı : {} ".format(f.encoding))

f.close()