#a = append modu / hiç yoksa yaratır varsa üstüne ekler
#w = write / hiç yoksa yaratır,varsa değiştirir(siler yeni yazdığını ekler)
#r = read /

#f.close()   # bu bir manada save demek(yani kaydet)

"""
bilmen gerekenler:

str.strip() (str karakter dizisinin başındaki ve sonundaki beyaz boşlukları
ve \n(enter) karakterlerini temizler )

str.split(...) (str yi tırnak içinde verilen karakterlerden böler ve her bir elemanı listeye ekler
ve sonuç olarak bize liste veriri)
"""

def getAges(file):
    fd=open(file,"r")
    lines = fd.readlines()
    for person in lines:
        person_age = person.split(" ")[3].strip() #strip ile enter i sildik
        print(person_age) #yanyana yapsın istemiyorsak ,end=" " yaparız
    fd.close()

getAges("ismail.txt")

"""
ahmet abasi e 45\n
mehmet babasi k 25

"""
