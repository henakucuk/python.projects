"""
kurallara uygun şifre belirleme kontrolü

kurallar:
8 karakterden az olamaz
en az 1 harf olmalı
en az 1 rakam olmalı
noktalama ve özel karakterler yok

while döngüsünü kullanarak kullanıcıdan bir şifre girmesini iste
girilen şifre yukarıdaki kurallara uygun olmadığı sürece
şifre belirlemeye devam etsin
kurallara uygun şifre belirlerle uygun şifre belirlediniz masajını yazdır
"""
"""
deneme = "ismail"
deneme.isalpha()  -> True (alpha mı?)
deneme = "ismail33"
deneme.isalpha()  -> False
deneme.isnumeric()  -> False  (numeric mi?)
deneme.isalnum() -> True  (hem alfabetik hemde numara içeriyor ise, ama özel karakterler ve noktalama işareti yok)
"""

while True:
    sifre = input("Bir şifre belirle") 
    if len(sifre) >= 8:
        if sifre.isalnum() == True and sifre.isalpha() == False and sifre.isnumeric() == False:
            print("Uygun şifre")
            break
        else :
            print("lütfen içinde en az 1 harf ve 1 rakam bulunan bir şifre girin")
    else :
        print("şifre uygun değil")
