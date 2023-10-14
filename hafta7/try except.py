
try:
    s1 = int(input("Birinci sayıyı gir"))
    opr = input("Operatör gir ör: +,-,/,*")
    s2 = int(input("İkinci sayıyı gir"))

    if opr == "/":
        sonuc = s1/s2
        print(sonuc)



except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
except ValueError:
    print("Bir değer girin")

finally:   #devamında bir şey yap anlamında
    print("Tekrar çalıştır")
