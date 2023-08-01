"""
kullanıcıdan günler için [0-6] ve aylar için [1-12] sayı alın.
karşılık gelen günü ekrana basın. sadece int ve sözlük değişkenlerine izin verilecek.
döngüye ihtiyacınız var ise while kullan.
örn: gün >> 1
     ay  >> 10
     pazartesi-ekim
"""

gün = int(input("gün girin [0-6] ör: pazar = 0"))
ay = int(input("ay giriniz [1-12] ör: ocak = 1"))
sözlükgunler = {0:"pazar",1:"pazartesi",2:"sali",3:"çarşamba",4:"persembe",5:"cuma",6:"cumartesi"}
sözlükaylar = {1:"ocak",2:"şubat",3:"mart",4:"nisan",5:"mayıs",6:"haziran",7:"temmuz",8:"ağustos",9:"eylül",10:"ekim",11:"kasım",12:"aralık"}
dongu = True

while dongu == True:
    print(f"{sözlükgunler[gün]}-{sözlükaylar[ay]}")
    dongu = False

