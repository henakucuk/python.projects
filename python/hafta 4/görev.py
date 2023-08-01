#len fonksiyonu bir str nin karakter sayısını veriyor bu fonsiyonu kullanmadan
#girilen bir verinin ne kadar uzun olduğunu ekrana yazdıran bir şey yaz for ile ör: ismail girildi girilen bu veri 6 karakter uzunluğundadır de


deneme = input("adınızı girin")
sayac = 0

for i in deneme:
    sayac = sayac + 1
print(f"Adınız {sayac} karakter uzunlugundadir")
