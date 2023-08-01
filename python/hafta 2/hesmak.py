"""
kullanıcıdan  1 nci sayıyı iste int tipinde input ile
kullanıcıdan operator iste +-*/ seklinde
kullanıcıdan 2 nci sayıyı iste int tipinde input ile
"""

sayi1 = int(input("birinci sayıyı gir"))
islem = input("operator gir ör: +-*/ gibi")
sayi2 = int(input("ikinci sayıyı gir"))


if islem == "+":
    sonuc = sayi1+sayi2
    print(sonuc)
elif islem == "*":
    sonuc = sayi1*sayi2
    print(sonuc)
elif islem == "/":
    if sayi2 == 0:
        print("bir sayı sıfıra bölünemez")
    else:
        sonuc = sayi1/sayi2
        print(sonuc)
elif islem == "-":
    sonuc = sayi1-sayi2
    print(sonuc)
else:
    print("sadece +-*/ gir")
