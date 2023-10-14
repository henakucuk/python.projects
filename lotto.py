"""1.kullanıcı 1,80 arasında 10 tane sayı seçer
2.çekiliş için 22 tane 1,80 arasından sayı seçilir
3.karşılaştır ve bana tutan adedi söyle
4.eğer tuttanlar 0,6,7,8,9,10 ise ödül var değilse boş
"""
"""
import random

sayilar = []
#sayılar 10 rakam

while len(sayilar)<10:
    sayi = random.randint(1,80)
    if sayi not in sayilar:
        sayilar.append(sayi)
    sayilar.sort()

print(sayilar)

#cekilis 22 rakam
cekilis = []

while len(cekilis)<22:
    sayi = random.randint(1,80)
    if sayi not in cekilis:
        cekilis.append(sayi)
    cekilis.sort()

print(cekilis)

sayac = 0
for eleman in sayilar:
    if eleman in cekilis:
        sayac = sayac+1
print(sayac)

if sayac in (0,6,7,8,9,10):
    print("ödül kazandın.")
else:
    print("ödül kazanılmadı")
"""
import random

def rastgelesayiuret(adet):
    liste = []
    while len(liste)<adet:
        sayi = random.randint(1,80)
        if sayi not in liste:
            liste.append(sayi)
        liste.sort()
    return liste

cekilis = rastgelesayiuret(22)

kasa = 5
for _ in range(1000):  #sayısı önemli değil anlamında bu : _
    kasa = kasa+5
    kolon = rastgelesayiuret(10)
    sayac = 0
    for eleman in kolon:
            if eleman in cekilis:
                sayac = sayac+1

    if sayac in (0,6,7,8,9,10):
        if sayac == 0:
            kasa = kasa-20
        elif sayac == 6:
            kasa=kasa-50
        elif sayac == 7:
            kasa = kasa-100
        elif sayac == 8:
            kasa = kasa-200
        elif sayac == 9:
            kasa = kasa-400
        elif sayac == 10:
            kasa = kasa-1000
    
print(kasa)
