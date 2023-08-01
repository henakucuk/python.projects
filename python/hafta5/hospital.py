"""
bir hastane kayıt sistemi için kişi ekleme yapılacaktır. kaç kişi ekleneceğini
ve kişi bilgilerini kullanıcıdan alıp saklayan programı  yaz.
(isim,soyisim,doğum tarihi,cinsiyet,ağrı şiddeti [0-10])

1: gerekli değişkenler tanımlanır
2:kullanıcıdan kaç hasta kayıdı yapacağını iste(minimum 3 kişi zorunlu)
3:girilen hasta sayısı kadar döngü kur(while döngüsü)
4:her bir döngüde kullanıcıdan bir kişinin bütün bilgileri iste
5:bir kişinin bütün bilgilerini sözlüğe ekle (ağrı şiddeti 0 ve 10 arasında olduğunun garantisini al)
6:sözlüğü listeye ekle
"""

patiens = []

number_of_records = 0

count = 0

patien_dictonary = {}

flag = True
flag2 = True

while flag == True:
    number_of_records = input("number of records >> ")
    if number_of_records.isdigit():   # == True demiyoruz çünkü bu da aynı anlama geliyor
        number_of_records = int(number_of_records)
        if number_of_records >= 3:
            flag = False
        else:
            print("please enter 3 or more than 3 record numbers")
    else:
        print("please write a number.")
count = 0
while count < number_of_records : #girilecek olan hasta sayısı kadar döngü kur
    name = input("what is your name  >> ")
    lastName = input("what is your last name? >> ")
    birthDate = input("what is your birthdate? [dd.mm.yyyy] >> ")
    gender = input("what is your gender? W/M >> ")
    tcNumber = input("what is your TC number? >> ")
    painIntansity = input("what is your pain intansity? [0-10] >> ")

    while flag2 == True :
        if painIntansity.isdigit():
            painIntansity = int(painIntansity)
            if painIntansity <= 10: #10 dan küçük olması yeter çünkü numeric/digit olması eksi(-) leri kabul etmiyor
                flag2 = False
            else:
                print("please enter a valid number")
        else:
            print("painIntansity should be between 1-10(inclusive)")
        
    patien_dictionary = {"name": name,"lastName": lastName,"birthDate":birthDate,"gender":gender,"tcNumber":tcNumber,"painIntansity":painIntansity}
    patiens.append(patien_dictionary)

for patien in patiens:
    print(f"{patien['name']}{patien['lastName']}{patien['birthDate']}{patien['gender']}{patien['tcNumber']}{patien['painIntansity']}")
