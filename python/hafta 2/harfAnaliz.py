"""
kullanıcıdan 1 harf iste o harfin sessiz sesli veya ing harf olup olmadığını denetle
lower kullanıcı hangi harfi büyük veya küçük girse bile onu küçük yapar
upper ise büyük
"""
eng = "qwx"
sesli = "aeıioöuü"

harf= input("Bir harf giriniz").lower()


if harf in sesli:
    print("girdiğin harf sesli harf")
elif harf in eng:
    print("girdiğin harf ingilizce harf")
else:
    print("girdiğin harf sessiz harf")
