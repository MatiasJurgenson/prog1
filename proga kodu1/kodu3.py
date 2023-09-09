def sünnikuupäev(kood): #'34501234215'
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"] #copysin wikist
    if int(kood[0]) < 4:
        aasta = 1900
    else:
        aasta = 2000
    return f"{kood[5:7]}. {kuud[int(kood[3:5])-1]} {aasta + int(kood[1:3])}"
print(sünnikuupäev('49812238394'))