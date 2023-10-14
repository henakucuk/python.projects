
def topla(s1,s2,*args):   #+s1 ve s2 yi göndermemiz zorunlu yapıyoruz böyle yaparak
    sonuc = 0     #+ ve buraya sonuc = s1 + s2 deriz
    
    for i in args:
        sonuc += i # sonuc = sonuc + i   ,,, bunun çalışması için sonuc = 0 diye yapmamız lazım

    return sonuc

print(topla())     # +   s1 ve s2 ekleyerek de bu ve bunun altındaki hata verir, bu ikisi eksik der
print(topla(5))    #5 +   bu ise sadece s2 eksik der
print(topla(5,10)) #15
print(topla(3,6,9))#18
________________________

def topla(s1=0,*args):
    sonuc = s1

    for i in rangs:
        sonuc += i

    return sonuc

print(topla())     #  çalışır
print(topla(5))    #5
print(topla(5,10)) #15
print(topla(3,6,9))#18
________________

print("ahmet",end="")
print("mehmet") # bu ikisi bize ahmet mehmet diye yanyana çıktı verir

sep="-" #aralarına - koyar(print sonuna yaz)
