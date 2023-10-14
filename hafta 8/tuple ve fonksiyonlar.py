def toplamaYap(s1,s2):
    sonuc = s1 + s2
    return sonuc

fonktanGelen = toplamaYap(3,5)

print(fonktanGelen)

___________________

def myPrint(m1="",m2="",m3=""):
    print(f"{m1},{m2},{m3}")


ptint("hena")

_____________________

#tuple denemenin çok benzeri ama append yapamıyorsun ve çıkartamıyorsun
#normal parantez ile yazıyorsun ()
# tuople yani demette sadece index(arama) yada count(sayma) kullanabiliyoruz
#demeti listeye çevirip düzenleyebiliyoruz a = list(demet) list yapıyor,böylece düzenleyebiliyoruz
#demeti liste yapsak bile demet hala tuple kalıyor a liste oluyor,demet değil(içindeki değerleri listeye çevirdik)
# demet2 = demet yapıp kopyalabiliyoruz (yani demetin içindekileri demet2 ye koyyalayabiliyoruz)

def myPrint(*gelenler):   #bu yıldız gelenleri tuple a çeviriyor,,kaç tane gönderirsem çalışsın istiyorsak bunu yapacağız
    print(type(gelenler)) #tuple
    for i in gelenler:
        print(i)

myPrint("ahmet",3,6,"hasan",1.14,{0:"pazar",1:"pazartesi"})
