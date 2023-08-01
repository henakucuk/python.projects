"""
len(jdfhbvgrhkmdcnbhfrjk)
len kaç karakter olduğunu sana söylüyor(20)
"""
#kullanıcıdan aks nin ikinci ve dördüncü karakterini ayrı ayrı iste
#aldığın verileri değişkendeki bilgi ile karşılaştır
#eğer doğru ise kullanıcıya giriş başarılı de değilse değil de

#anne kızlık soyadı = aks
aks = "kuzucu"
harf2= input("Anne kızlık soyadının ikinci harfini gir")
harf4 = input("Anne kızlık soyadının dördüncü harfini gir")

"""
aks_2 = aks[1]
aks_4 = aks[3]

burada yukarıdakini yapma sebebimiz ilerde ihtiyaç duyarız diye tanımlamak

if harf2 == aks_2 and harf4 == aks_4:
    print("giriş başarılı")
else:
    print("hatalı giriş")
"""

if harf2 == aks[1] and harf4 == aks[3]:
    print("giriş başarılı")
else:
    print("hatalı giriş")
