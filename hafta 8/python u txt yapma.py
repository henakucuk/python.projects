#a = append modu / hiç yoksa yaratır varsa üstüne ekler
#w = write / hiç yoksa yaratır,varsa değiştirir(siler yeni yazdığını ekler)
#r = read /

f=open("ismail.txt","r")
icerik = f.read()

f.close()   # bu bir manada save demek(yani kaydet)

def getAges():
    pass

getAges("ismail.txt")
