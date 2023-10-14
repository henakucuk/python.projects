"""
ek anlatım tür dönüşümleri
kullanıcıdan veriyi hangi tipte istersen iste o veriyi tip dönüşümü yaptığın s-
ör: integer tipinde inputtan gelen veriyi len() fonksiyonu ile sayamazsin bunu-
tür dönüşümleri veri = 3 -> str(veri) şeklinde yapılır.
"""

"""
en az 1 harf,en az 1 rakam ve 8 karakterden küçük olmayan şifre

durum = 0

while durum == 0:
    sifre = input("lütfen bir şifre beirleyin: ")
    if len(sifre)>= 8 and sifre.isalnum:
        print("Kurallara uygunn şifre belirlediniz")
        durum = durum + 1
    else:
        print("Hata")

"""

"""
üç kere deneme hakkı olan şifre doğrulama
sifre = "Gifted12"
hataSay = 0

while hataSay < 3:
    girilenSifre = input("Lütfen şifre giriniz: ")
    if girilenSifre != sifre:
        hataSay = hataSay + 1
        print(f"Kalan hakkınız: (3-hataSay)")
    else:
        print("Tebrikler doğru şifre girdiniz")
        break
if hataSay == 3:
    print("3 kez hatalı şifre girdiniz")

"""


"""

#manuel tutulan
tutulan = "74"
tahmin = "0"

while tahmin != tutulan :
    tahmin = input("Tahmini gir?: ")
    if tahmin < tutulan:
        print("çık")
    elif tahmin > tutulan:
        print("in")
print("tebrikler")


"""
"""

#random tutulan
import random

tutulan = random.randint(0,100)
tahmin = 0

while tahmin != tutulan:
    tahmin = int(input("Tahmini gir?: "))
    if tahmin < tutulan:
        print("çık")
    elif tahmin > tutulan:
        print("in")
print("tebrikler")

"""
"""
#sayaçlı hali
import random
tutulan = random.randint(0,100)
tahmin = 0
sayac = 0
while tahmin != tutulan:
    tahmin = int(input("Tahmini gir?: "))
    sayac = sayac + 1
    if tahmin < tutulan:
        print("Çık")
    elif tahmin > tutulan:
        print("İn")
print(f"Tebrikler {sayac} kerede bildin")
"""





