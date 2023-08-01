"""
yazbel.com

import la random kütüphanesini ekle
randint = random kütüphanesinden integer seç

help(random.randint) dersen sana açıklama yapar
"""
import random
s1 = -1500

tutulan = random.randint(0,100)  #0 ve 100 dahil olmak üzere ve arasında bir sayı seç

while s1 != 10:
    tahmin = int(input("Bir sayı tuttum tahmin et"))
    if tahmin < tutulan:
        print("cik")
    elif tahmin > tutulan :
        print("in")
    else:
        print("tebrikler")
        s1 = 10

#s1 10 a eşit olmadığı sürece devam edecek. bu yüzden else te doğru bildiğinde s1 i 10a eşitliyoruz
#çünkü eşitlemezsek hala devam eder(bilsek bile)
"""
import random

tutulan = random.randint(0,100)  #0 ve 100 dahil olmak üzere ve arasında bir sayı seç

while tutulan != tahmin:
    tahmin = int(input("Bir sayı tuttum tahmin et"))
    if tahmin < tutulan:
        print("cik")
    elif tahmin > tutulan :
        print("in")
    else:
        print("tebrikler")
        tutulan = tahmin
"""

    
