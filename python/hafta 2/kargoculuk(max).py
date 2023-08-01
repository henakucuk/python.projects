"""
kullanıcıdan bir ağırlık iste
kullanıcıdan bir hacim iste
max fonksiyonunu kullanarak büyük olanı tespit et
eğer büyük olan ağırlık ise kullnıcıya kargonuz ağırlıya göre hesaplandı yaz
eğer tam tersi ise kullanıcıya kargonuz hacme göre hesaplandı yaz
"""
agirlik = int(input("Agirlik gir"))
hacim = int(input("Hacim gir"))

buyukOlan = max(agirlik,hacim)

if buyukOlan == agirlik:
    print("Kargonuz agirliga göre hesaplandı")
else:
    print("Kargonuz hacme göre hesaplandı")

