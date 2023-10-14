import subprocess as sp

hangiprogram = input("Bir program adı gir. ör:notepad ->  ")
hangiprogram = hangiprogram + ".exe"
sp.call(hangiprogram)




"""
python dosyasını exe haline çevirmek için
1.cmd ekranında python dosyanızın olduğu dizine gidin
2.cmd ekranına pyinstaller dosyaismi.py --onefile --noconsole

komutunu yazın, yeni oluşmuş klasörler arasındaki dist klasörünün içinde python dosyanızın
exe ye çevrilmiş halini göreceksiniz

eğer herhangi bir modül bilgisayarınızda bulunmazsa
cmd ekranında pip install modulAdi komutu ile ilgili mudülü kurabilirsiniz
doğru modül isminin ne olduğunu google veya pypi.org adresinden araştırabilirsiniz

"""
