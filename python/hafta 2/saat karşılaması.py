
"""kullanıcıdan bir sayı iste ör:7
eğer girilen sayı 6 dahil ve 12arasındaysa kullancııya günaydın de
eğer 12 dahil ile 17 arasındaysa iyi günler de
eğer 17 dahil ile 21 arasındaysa iyi akşamlar de
eğer 21 dahil ile 6 arasındaysa iyi geceelr de
"""

sayi = int(input("Saat kaç?"))

if sayi>=6 and sayi<12:
    print("Günaydın")
elif sayi>=12 and sayi<17 :
    print("iyi günler")
elif sayi>=17 and sayi<21 :
    print("iyi akşamlar")
else:
    print("iyi geceler")

