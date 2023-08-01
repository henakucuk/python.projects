"""
90 ve 100 aralığı (90 ve 100 dahil) AA
80 e eşit ve yüksek 90dan düşük BA
70 e eşit ve yüksek 80dan düşük BB
60 e eşit ve yüksek 70 den düşük CB
50 ye eşit ve yüksek 60 dan düşük CC
0 a eşit ve yüksek 50 den düşük FF

kullanıcıdan not iste ör:72 girdiği  notun harf karşılığını kullanıcıya söyle
"""

puan = int(input("Notunu gir ör:72"))

if puan>=90:
 print("Notun AA")
elif puan>=80 and puan<90:
    print("Notun BA")
elif puan>=70 and puan<80:
    print("Notun BB")
elif puan>=60 and puan<70:
    print("Notun CB")
elif puan>=50 and puan<60:
    print("Notun CC")
else:
    print("Notun FF")
