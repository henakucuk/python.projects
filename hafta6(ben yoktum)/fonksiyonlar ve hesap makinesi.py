"""
# def = definititon

def selamVer(x):     #burada x yerine istedğimizi yazabiliriz,bir önemi yok (bunu print etsek basmaz)
    print(f"Merhaba {x}")

isim = input("İsim gir")


selamVer(isim) #önemli olan buraya ne yazdığımız,buraya yazdığımız x yerine oturuyor

"""
"""
def selamVer(x,y):
    print(f"Merhaba {x}{y}")

isim = input("isim gir")
soyisim = input("soyisim gir")

selamVer(isim,soyisim) #sıralama önemli


"""
"""

def selamVer(x,y):
    return x,y  #x ve y yi dışarı atıyoruz,,,böylece print yapabiliriz

isim = input("isim gir: ")
soyisim = input("soyisim gir: ")

print(f"Merhaba{selamVer(isim,soyisim)}")

"""
def toplamaYap(s1,s2):
    sonuc = s1+s2
    return sonuc # bu sonucu dısarı atıyor

def cikarmaYap(s1,s2):
    sonuc = s1-s2
    return sonuc

def carpmaYap(s1,s2):
    sonuc = s1*s1
    return sonuc

def bolmeYap(s1,s2):
    sonuc = s1/s2
    return sonuc

sayi1 = int(input("birinci sayiyi gir"))
opr = input("operator gir ör: +-*/")
sayi2 = int(input("ikinci sayiyi gir"))

if opr == "+":
    print(toplamaYap(sayi1,sayi2))
elif opr == "-":
    print(cikarmaYap(sayi1,sayi2))
elif opr == "*":
    print(carpmaYap(sayi1,sayi2))
elif opr == "/":
    print(bolmeYap(sayi1,sayi2))
