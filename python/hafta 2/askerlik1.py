"""kullanıcıdan cinsiyet iste  E veya K şeklinde kullanıcıdan int yaş iste
askere gidebilmek için erkek olmak ve 20 yaşından büyük veya eşit olmak gerek ve 65 yaşından küçük
kişinin girdiklerine göre askere gidebilme durumunu ekrana yazdır
"""

cinsiyet = input("Cinsiyet Gir E/K")

if cinsiyet == "K" :
    print("Kadınlar askerlikten muaftır")
elif cinsiyet == "E":
    yas = int(input("Yasın Kac?"))
    if yas >= 20 and yas<65:
        print("Askere Gidebilirsin!")
    else:
        print("Askere Gidemezsin")

else:
    print("Hatalı Veri Girdiniz")
