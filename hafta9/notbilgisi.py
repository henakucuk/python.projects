"""
kullanıcıdan 3 adet not bilgisi iste ör:50-60-90
aldığın bilgileri notlar.txt dosyasına kaydet
daha sonra notlar.txt dosyasından girilen notları oku
ortalamasını bul ekrana yazdır

bu kodu fonksiyonel yaz

yapılacak işler fonksiyonlarla yapılsın

dosya bulunamadı gibi hatalara çözüm bul

kodda en az 3 fonksiyon olacak

"""
fname = "C:\\Users\\LENOVO\\Desktop\\dosya\\db\\notbilgisi.txt"

def getValues(number):
    notList = []
    for i in range(number):
        myNote = input("Enter a note -> ")
        notList.append(myNote)
    return notList

def saveValues(notes):
    f = open(fname,"w")
    for i in notes:
        f.write(i)
        f.write("\n")
    f.close()

def readValues():
    try:
        f = open(fname,"r")
        toplam = 0
        sayac = 0
        for i in f.readlines():
            sayac += 1
            toplam = toplam + int(i.strip())
        print(toplam/sayac)

    except FileNotFoundError:
        print("There is not such a file")

x = getValues(3)
saveValues(x)
readValues()
