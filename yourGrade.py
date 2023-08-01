puan = input("Notunu gir ör:72")

if puan.isdigit() == True:
    puan = int(puan)
    if puan >= 90:
        print("noyun AA")
    elif puan >= 80 and puan < 90:
        print("notun BA")
    elif puan >= 70 and puan < 80:
        print("notun BB")
    elif puan >= 60 and puan < 70:
        print("notun CB")
    elif puan >= 50 and puan < 60:
        print("notun CC")
    elif puan >= 0 and puan < 50:
        print("notun FF")
else:
    print("lütfen puanınızı düzgünce giriniz")

#(değiştirdim,saçma bir şey yazınca hata veriyordu)
