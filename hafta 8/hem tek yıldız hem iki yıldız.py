
def funcTest(*args,**kwargs):
    for i in args:
        print(i)

    print("-"*30)

    for k,v in kwargs.items():
        print(k,"\t",v)

funcTest(23,'E',"manisa","abuzer",alan = 1.23 , pi = 3.14, yas = 86,isim="ahmet")

"""
çıktı bu:

23
E
manisa
abuzer
------------------------------
alan 	 1.23
pi 	 3.14
yas 	 86
isim     ahmet
"""
