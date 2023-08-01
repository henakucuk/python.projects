"""
oyuncu 1 için hamle iste ör: taş veya kağıt veya makas şeklinde
oyuncu 2 için hamle iste ör: taş veya kağıt veya makas şeklinde
taş : taş = berabere
taş : kağıt = oyuncu 2 kazandı
taş : makas = oyuncu1 kazandı
kağıt : taş = oyuncu 1 kazandı
kağıt : kağıt = berabere
kağıt : makas = oyuncu 2 kazandi
makas : taş = onyuncu 2 kazandi
makas : kağıt = oyuncu 1 kazandı
makas : makas = berabere
"""

oyuncu1 = input("Oyuncu 1:Bir hamle giriniz ör:taş,kağıt,makas")
oyuncu2 = input("Oyuncu 2:Bir hamle giriniz ör:taş,kağıt,makas")

if oyuncu1 == oyuncu2:
    print("berabere")
elif oyuncu1 == "kagit" and oyuncu2 == "tas" or oyuncu1 == "tas" and oyuncu2 == "makas" or oyuncu1 == "makas" and oyuncu2 == "kagit":
    print("oyuncu 1 kazandi")

elif oyuncu1 == "tas" and oyuncu2 == "kagit" or oyuncu1 == "kagit" and oyuncu2 == "makas" or oyuncu1 == "makas" and oyuncu2 == "tas":
    print("oyuncu 2 kazandi")
else:
    print("lütfen hamlenizi ingilizce karakterle  yazınız")
