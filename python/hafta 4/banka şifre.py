"""
atm nin bildiği şifreyi 3 deneme hakkıyla bilmeye çalışıyorsun
"""

sifre = "Gifted13"
durum = True
sayac = 0

while durum == True:
    girilen = input("şifreyi gir")
    if sifre != girilen:
        print("yanlis giris")
        sayac = sayac +1
        if sayac == 3:
            print("3 deneme hakkida kullanıldi")
            durum = False
    else:
        print("giris basarili")
        durum = False
        print("sisteme hoş geldin")
"""
sifre = "Gifted13"
hataSay = 0

while hataSat < 3:
 girilenSifre = input("Sifrenizi giriniz")
 if girilenSifre != sifre:
  hataSay = hataSay + 1
  print(f"Yanlis sifre girdiniz kalan hakkınız {3-hataSay}")
 else:
 print("Tebrikler,dogru girdiniz")
 break

if hataSay == 3:
 print("3 kez hatalı şifre girdiniz...")
"""
