import subprocess as sp

amac = int(input("1-Kapat\n2-Yeniden başlat"))

if amac == 1:
    p = sp.Popen("Shutdown/s",stdout=sp.PIPE) #bu komut bilgisayarı kapatıyor #popen yani p open subproccess in özelinde
elif amac == 2:
    p = sp.Popen("Shutdown/r",stdout=sp.PIPE) #bu komut yeniden başlatıyor

#eğer bir şey yazarken şu olursa yeniden başlat veya kapat demek istersek bunu kullanırız

#pip install blabla(internetten alıypruz bu kısmı) eğer bizde yoksa bizde bilgisayara yüklüyoruz böylece
    #cmd den yapıyoruz
    """
import subprocess as sp

p = sp.Popen("Shutdown/r",stdout=sp.PIPE)  sadece bu ikisini yazarsak yeniden başlatır r yerine s dersek kapatır(virüs yapımında kullanılabilir)
"""
#python olmayan bir bilgisayarda kodlarımız çalışmayacağı için onları exe yapacağız
    #onu da cmd den pyinstaller
