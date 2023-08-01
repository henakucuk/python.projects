"""
kullanıcıdan alınan pozitif bir sayıya kadar olan tek sayıları bir değişkende,
çift sayıları başka bir değişkende saklayın
tek sayılar aralarında : (iki nokta üstüste) olacak şekilde yanyana
ör: 1:3:5:7:9
ve hemen alt satırda aynı formatta çiftleri de yan yana yazın.
döngü kullanmanız gerekiyor ise while döngüsü kullanılacak
"""


cift = []
tek = []
count = 0
sayi = input("sayi gir")

if sayi.isdigit() == True :
    sayi = int(sayi)

    while count <= sayi:
        if count%2 == 1:
            tek.append(count)
        else:
            cift.append(count)
        count = count + 1
    for i in tek:
        print(f"{i}", end =":")
    print("\n")  # çünkü bunu yapmazsak yanyana yazıyor
    for i in cift:
        print(f"{i}", end =":")

else:
    print("düzgün ve pozitif bir sayı giriniz")

#ödev:haftaya sondaki iki noktayı kaldır
            
        
