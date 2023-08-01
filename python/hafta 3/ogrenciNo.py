"""
örnek öğrenci numarası 22-156-025
22 kayıt yılını
156 bölümünü
025 kayıt sırasını

girilen öğrenci numarası 10 karakterden az veya çok olamaz
kullanıcıdan aldığın 10 karakterli(- işareti dahil)öğrenci numarasını parçala
ve yukarıdaki bilgilere göre ekrana yazdır,çıktı tek print ile olacak

örnek çıktı: 2022 yılında 156 nolu bölüme 025 sıra numarası ile kayıt oluşturmuş bir öğrencisiniz
"""

ogrenciNo= input("Lütfen öğrenci numarasını giriniz ör:22-156-025")

kayitYili= ogrenciNo[0:2]
bolumu= ogrenciNo[3:6]
kayitSira= ogrenciNo[7:]

if len(ogrenciNo) == 10:
    print(f"20{kayitYili} yılında,{bolumu} numaralı bölüme, {kayitSira} sıra numarası ile kayıt oluşturmuş bir öğrencisiniz")

else:
    ("Lütfen düzgün giriniz")
