"""
kelime="giftedcoder"
kelime[:1]
=g der yani 0 ı alır
kelime[2:]
=ftedcoder
kelime[1:6]
=ted
"""
#kelime="abuzittin"
#kelime[5:7] beşten yediye kadar
#=tt

"""
1TR331234567
organik=0
gezen=1
kümes=2

kullanıcıdan yumurta kodu iste
aldığın koduhn ilk karakterini yukarıdaki açıklamaaya göre karşılaştır
ve yumurta türünü beirle
kodun 2nci ve 3üncü karakteri ülke kodu olarak belirle
kodun 4üncü ve 5inci karakteri şehir kodu olarak belirle
kodun 6ncı karakter ve sonrasını işletme kodu olarak belirle
bu kodun 12 karakterden az veya çok olmaması gerekiyor

ayrıştırdığın verileri şu formatta ekrana yazdır

"Bu yumurta ör:Organiktir ve Türkiyenin Mersin ilinde 1234567 numaralı işletme
tarafından üretilmiştir"
"""
"""
kişinin tr ve 33 girmesini zorunlu hale getir ve girmezse uyar
"""

yumurtaKodu= input("Lütfen yumurta kodunu giriniz") #1TR331234567


yumurtaTuru = yumurtaKodu[0]
ulkesi = yumurtaKodu[1:3]
sehir = yumurtaKodu[3:5]
isletme = yumurtaKodu[5:]

if len(yumurtaKodu) == 12:
    if yumurtaTuru == "0":
        yumurtaTuru = "organik"
    elif yumurtaTuru == "1":
        yumurtaTuru = "gezen"
    elif yumurtaTuru == "2":
        yumurtaTuru = "kümes"

    if ulkesi == "TR":
        ulkesi = "Türkiye"
        if sehir == "33":
            sehir = "Mersin"
            print(f"yumurta türü {yumurtaTuru}, ülkesi {ulkesi} ve {sehir} şehrinin {isletme} numaralı işletmesi tarafından üretilmiştir")
        else:
            print("lütfen 33 girin")
            
    else:
        print("lütfen TR giriniz")

else:
    print("Girilen kod hatalı")
        

   
