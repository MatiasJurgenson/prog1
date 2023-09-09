import math

# copysin moodlist oma kodutöö sest tegin viimased muudatused koodile seal
def info_isikukoodist(kood): #'34501234215' '39911295661'
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"] #copysin wikist
    print(f"Lugesin isikukoodist {kood} välja järgmised andmed: ")
    if int(kood[0]) % 2 == 0:
        print("Sugu: Naine")
    else:
         print("Sugu: Mees")
    
    if int(kood[0]) <= 2:
        aasta = 1800
    elif int(kood[0]) <= 4:
        aasta = 1900
    else:
        aasta = 2000
    print(f"Sünnikuupäev: {kood[5:7]}. {kuud[int(kood[3:5])-1]} {aasta + int(kood[1:3])}")
    
    arv = int(kood[9:12])
    if arv >= 1 and arv <= 10:
        haigla = "Kuressaare haigla"


#info_isikukoodist("39911290011")
def on_korrektne_isikukood(sone):
    summa = 0
    
    for i in range(10):
        if i + 1 == 10:
            summa += int(sone[i])
        else:
            summa += (i+1)*int(sone[i])
    summa = math.floor(summa % 11)
        
    if summa == 10: #kui jääk peaks olema 10
        summa = 0
        for i in range(10):
            if i + 3 >= 10:
                
                summa += (i-6)*int(sone[i])
            else:
                summa += (i+3)*int(sone[i])
        summa = math.floor(summa % 11)
        if summa == 10:
            summa = 0
            
    return summa == int(sone[-1])
isikukood = str(input("Palun sisestage isikukood: "))
if on_korrektne_isikukood(isikukood):
    info_isikukoodist(isikukood)
else:
    print("isikukood pole korrektne")
    