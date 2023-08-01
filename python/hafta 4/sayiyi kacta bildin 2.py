import random
sayac=0
durum = -5

tutulan=random.randint(0,100)

while durum != 10:
    sayi= input("0 ile 100 aralığında bir sayı seç")
    if sayi.isdigit() == True:
        sayi = int(sayi)
        if sayi < tutulan:
            print("cik")
            sayac = sayac +1
        elif sayi > tutulan:
           print("in")
           sayac = sayac +1
        else:
            sayac = sayac +1
            print(f"tebrikler {sayac} kerede bildin")
            durum = 10
    else:
        print("lütfen rakamlarla düzgün bir sayı giriniz")
