bilgi = """
Pisagor Üçlüsü a<b<c ve a^2 + b^2 = c^2 olarak tanımlanabilir.
Örneğin ==> 3^2 + 4^2 = 9+16 = 5^2 = 25
a + b + c = 1000 sonucunu veren yukarıdaki kurala uyan yalnızca bir adet pisagor üçlüsü vardır.
Bu üçlü için (a * b * c) kaçtır?
 """

def pisagor_uclusu():
    for a in range(1,1000):

        for b in range(a+1,1000):
            c=1000-a-b

            if(a**2+b**2==c**2):
                print("Bu uclu ==> a = {} , b = {} , c = {}".format(a, b, c))

                return(a*b*c)


print(bilgi)
print("Carpimlari = {}".format(pisagor_uclusu()))