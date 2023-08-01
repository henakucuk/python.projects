"""
for döngüsü kullanarak kullanıcıdan 5 defa yaş bilgisi iste
aldığın bu yaşları "sakla" (saklama yöntemini iyi düşün)

alınan yaşların ortalamasını hesapla

ekrana iki ayrı satırda mesaş yazdır

1nci satırda hesapladığın ortalamayı yastır ör:"girilen yaşların ortalaması:32"
2nci satırda girilen en küçük yaş ile en büyük yaşı yazdır ör:"en küçük yaş:8 en büyük:12"
"""
yaslar = []

for i in range(5):
  yas =  int(input("Yaş giriniz"))
  yaslar.append(yas)

yaslar.sort()
toplam = 0

for i in yaslar:
    toplam = toplam + i

print("Ortalama:",toplam/5)
print(f"En küçük yaş:{yaslar[0]} En büyük yaş:{yaslar[-1]}")


"""
for i in ismail:
 print(i)
"""
