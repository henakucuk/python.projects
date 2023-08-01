weight = input("ağırlık gir")
volume = input("hacim gir")

if weight.isdigit() == True and volume.isdigit() == True:
    weight = int(weight)
    volume = int(volume)
    buyukOlan = max(weight,volume)
    if buyukOlan == weight:
        print("ağırlığa göre hesaplandı")
    else:
        print("hacime göre hesaplandı")
else:
    print("lütfen sayı ile giriniz")

