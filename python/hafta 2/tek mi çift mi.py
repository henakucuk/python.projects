#kullanıcıdan bir sayı iste verilen sayının çifr mi tek mi olduğunu ekrana yazdır
"""ipucu: geçen hafta gördiğimüz % mod alma operatörunu kullan
"""
sayi = int(input("bir sayı yaz"))
if sayi%2==0:
    print("sayı çifttir")
else:
    print("sayi tektir")
