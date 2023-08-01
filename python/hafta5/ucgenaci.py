"""
kullanıcıdan bir üçgenin iç açılarından ikisini isteyin,
üçüncü açıyı bulup ekrana yazın. kullanıcı programdan çıkmak isterse "q" veya
"Q" girmelidir. döngü kullanılacak ise while zorunlu
"""

cikis = ""
#flag = True
#sonra while içine -> flag == True: diyoruz
#veya deriz ki while içine -> cikis != "q" and cikis != "Q": 

while cikis.lower() != "q" :
    aci1 = float(input("Üçgenin  bir açısını gir,virgüllü ifade kullanmayın"))
    aci2 = float(input("Üçgenin diğer açısını gir,virgüllü ifade kullanmayın"))

    aci3 = 180 - (aci1 + aci2)

    print(f"girdiğiniz üçgende bilinmeyen üçgenin açısı = {aci3}")
    cikis = input("çıkmak istiyorsanız q veya Q ya basın")
#en sona da flag = False diyoruz
