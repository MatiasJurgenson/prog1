from urllib.request import urlopen



#{'USD': 0.9993, 'GBP': 0.8714, 'PLN': 4.6865}
def valuuta(sõnastik):
    suursõnastik = {}
    for võti, väärtus in sõnastik.items():
        ajutine = {}
        vahetus = 1 / väärtus
        for võti2, väärtus2 in sõnastik.items():
            if võti == võti2:
                pass
            else:
                ajutine[võti2] = round(vahetus * väärtus2, 4)
                
        ajutine['EUR'] = round(vahetus, 4)
        suursõnastik[võti] = ajutine
    suursõnastik['EUR'] = sõnastik
    return suursõnastik

url = "https://courses.cs.ut.ee/2022/programmeerimine/fall/uploads/Main/kursid.txt"
response = urlopen(url).read().decode("utf-8").split("\r\n")[:-1]


valuutasõnastik = {}
for asi in response:
    
    andmed = asi.split('\t')
    valuutasõnastik[andmed[0]] = float(andmed[2])
        
#print(valuutasõnastik)
lõpp = valuuta(valuutasõnastik)
    
    
while True:
    lähtevaluuta = str(input("Sisestage lähtevaluuta: "))
    if lähtevaluuta == "":
        break
    
    sihtvaluuta = str(input("Sisestage sihtvaaluta: "))
    if sihtvaluuta == "":
        break
    try:
        vahetatav = float(input("Sisestage vahetatav summa: "))
    except:
        break
    print("Selle raha eest saab", lõpp[lähtevaluuta][sihtvaluuta] * vahetatav, sihtvaluuta)
    