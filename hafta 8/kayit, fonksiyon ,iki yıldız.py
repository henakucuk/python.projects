
def kayitOlustur(**bilgiler):   #iki yıldız dict yapıyor
    print("-"*30)

    for anahtar,deger in bilgiler.items():
        print("{}:{}".format(anahtar,deger))

    print("-"*30)

kayitOlustur(ad="hena",soyad = "kucuk",sehir="Turkey",tel=1234567,boy = 1.75,kilo=53)  #keyler str oluyor ama value lar ne verirsek o olarak kalıyor
