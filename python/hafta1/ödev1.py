"""
kullanıcıdan yaş iste
eğer girilen yaş 18e büyük eşitse kullanıcıya ehliyet alabilirsin mesajını yazdır
"""
yas= int(input("Yasin ne?"))

if yas>=18:
    print("Ehliyet alabilirsin!" )

if yas<18:
    print("Seneye tekrar dene :) ")
