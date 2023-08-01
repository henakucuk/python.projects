"""
random kütüphanesini içe aktar
tutulan değişkenine 0-100 aralığında bir sayı tuttur

while döngüsünü kullanarak kullanıcıdan bir sayı girmesini iste
eğer kullanıcının girdiği sayı tutulandan büyükse kullanııya çık de
eğer kullanıcının girdiği sayı tutulandan küçükse kullanııya in de
eğer kullanıcının girdi sayı tutulana eşitse kullanıcıya "tebrikler ...kerede bildin" de
"""

import random
sayac=0
durum = -5

tutulan=random.randint(0,100)

while durum != 10:
    sayi=int(input("0 ile 100 aralığında bir sayı seç"))
    if sayi < tutulan:
        print("cik")
        sayac = sayac +1
    elif sayi > tutulan:
        print("in")
        sayac = sayac +1
    else:
        sayac = sayac +1
        print(f"tebrikler {sayac} kerede bildin")
        durum = 10
