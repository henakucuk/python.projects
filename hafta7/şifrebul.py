#have i been pwned
#sonda ekranın kapanmaması için input() koy,,bu soru sorar ve bekler böylece ekran kapanmaz
wordList = "0123456789"
sifre = "1037"
#birinci ikinciyi üçüncü dördüncüyü dürdüncü kendisinin bitirmesini bekler
for birinci in wordList:
    for ikinci in wordList:
        for ucuncu in wordList:
            for dorduncu in wordList:
                rakam = birinci + ikinci + ucuncu + dorduncu
                print(rakam,"Denendi")
                if rakam == sifre:
                    print("Sifre bulundu:", rakam)
                    input()
            
