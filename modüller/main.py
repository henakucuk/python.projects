#from dosya import * = bütün dosyalar
# bilgisayara *.txt yazarsak ta sadece o uzantıları getirir

import dosya
#import dosya as dp #adını kısaltıyoruz
#from dosya import toplamaYap
#from dosya import toplamaYap , ciftmi
#from dosya import*


dosya.selamVer("ismail")

def selamVer(isim):
    print("Selam",isim)

selamVer("ahmet")


print(dosya.toplamaYap(3,5))

print(dosya.ciftmi(5))
