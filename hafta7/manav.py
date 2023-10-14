"""
stackoverflow
#dir(dict)
manav otomasyonu
menü:
1.kayıt ekle
2.kayıt düzelt
3.kayıt ara
4.tümünü listele
5.kayıt sil
6.tümünü sil
0.çıkış yap
"""
#meyve adını isteyeceğin bir fonksiyon yarat
#meyveAdiSor() gibi
#fonksiyonel hale getireceksin
meyveler = {}
giris = -1

while giris != 0:
    giris = input("1:kayıt ekle,2:kayıt düzelt,3:kayıt ara,4:tümünü listele,5:kayıt sil,6:tümünü sil,0:çıkış yap -->>")
    if giris == "0":
        quit() #break ile aynı
    elif giris == "1":
        meyveAdi = input("Meyve adini gir -> ")
        if meyveAdi not in meyveler.keys():
            fiyati = input("Fiyat gir -> ")
            meyveler[meyveAdi] = fiyati #burada meyve adini fiyata sözlükte tanımlıyoruz
            print("Ürün eklendi")
        elif meyveAdi in meyveler.keys():
            print("Böyle bir ürün zaten var")
    elif giris == "2":
        meyveAdi = input("Meyve adi gir -> ")
        if meyveAdi in meyveler.keys():
            fiyati = input("Yeni fiyatı gir -> ")
            meyveler[meyveAdi] = fiyati
            print("Güncelleme yapıldı ")
        else:
            print("Olmayan şeyi düzeltemezsin")
    elif giris == "3":
        meyveAdi = input("Meyve adi gir -> ") #üzüm
        durum = meyveler.get(meyveAdi,"Böyle bir ürün yok")  #getir,al
        print(f"Meyve Adı: {meyveAdi} Fiyatı: {durum}")
    elif giris == "4":
        for i in meyveler.keys():  #meyvelerin keyslerine gidiyor(adlarına)
            print(i,meyveler[i]) #meyveler[i] bize fiyatı veriyor,,, i ise meyveleri,,o yüzden böyle yazıyoruz
    elif giris == "5":
        meyveAdi = input("Meyve adı gir -> ")
        durum = meyveler.pop(meyveAdi,"Böyle bir meyve yok")
        print(f"Meyve adi:{meyveAdi} - Fiyatı:{durum}  ---   Ürün Silindi")
    elif giris == "6":
        meyveler.clear()
        print("Tüm ürünler silinmiştir")
