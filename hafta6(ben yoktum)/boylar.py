
boylar = []

for x in range(8):
    boy = int(input("Boy gir"))
    boylar.append(boy)

boylar.sort()
toplam = 0
for herbirkisininboyu in boylar:  #tüm boyları listeler
    toplam = toplam + herbirkisininboyu #boyların toplamı

print("Ortalama",toplam/8)

print("En kısa boy",boylar[0],"En uzun boy",boylar[-1])

#harf yazınca hata veriyor
