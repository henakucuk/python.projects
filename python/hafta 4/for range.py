"""
for i in range(8):   (range dönüş sayısı) (i = işçi(üstüne yük yüklenen bir işçi)(i yerine başka bir şey ör:mehmet fln yazabilirsin))

deneme="ismail"

 for i in deneme:
  print(i)
-> i(işçi) ilk seferde birinci eleman olan i yi ikinci seferde s yi diye devam ediyor takii bitene yani l harfini yazana kadar
(hepsini alt alta teker teker yazıyor)
i
s
m
a
i
l
(yani dönüş sayısı ismailin harfleri(karakter sayısı) kadar)
"""
"""
for i in range(8):
 print("ismail")       (ekranna alt alta 8 kez ismail yazar ama yazmaya 0dan başlar)


for isci in range(8):
 print(f"{isci} ismail")
->
0 ismail
1 ismail
2 ismail
3 ismail
4 ismail
5 ismail
6 ismail
7 ismail
(8 tane,ama 0dan başlıyor)
"""
# list(range(8)) range bize liste üretiyor -> [0,1,2,3,4,5,6,7]
# list(range(5,10))    -> [5,6,7,8,9]
# for i in  range(8):
#  print(i)            -> alt alta 0dan 7ye kadar

"""
range de ikişer ikişer adım atabiliriz
for i in range(5,10,2):  -> alt alta 5,7,9
"""

durum = False
text = input("Bir kelime giriniz")

for i in text:
    if i == "?":
        durum = True

if durum == False:
    print("soru işareti yok")
else:
    print("soru işareti var")

