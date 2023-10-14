#kendisine gelen bilgileri ekrana alt alta yazacak
def funcTest(**kwargs):

    for keys in kwargs.keys():   #keys yazmadan da keysler çıkıyor
        print("{}".format(keys))
    print("-"*30)
    
    for keys,values in kwargs.items():
        print("{} \t{}".format(keys,values))

    print("-"*30)
    for values in kwargs.values():
        print("{}".format(values)) #print(deger)demek yeterli

funcTest(elma=3.250,armut=4,nar=6.3) #mesela burada elmayı "" içine alıp yazsaydık hata veriridi çünkü soldakini alıp sağdakine koyuyor yani sola "" koyamazsın

"""
çıktı bu olacak:

elma
armut
nar
---------------
elma 3.250
armut 4
nar 6.3
---------------
3.250
4
6.3
"""
