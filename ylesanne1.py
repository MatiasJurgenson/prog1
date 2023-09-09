def loe_failist(f):
    sõnastik = {}
    with open(f, encoding = "utf-8") as fail:
        nimekiri = []
        for rida in fail:
            rida = rida.strip().split(",")
            nimekiri.append(rida)
    for jär in nimekiri:
        minisõnastik = {}
        if jär[0] not in minisõnastik:
            for i in nimekiri:
                if i[0] == jär[0]:
                    minisõnastik[i[2]] = float(i[1])
            sõnastik[jär[0]] = minisõnastik
           
    return sõnastik

sõn = loe_failist("hinnakiri.txt")
print("Kaupluses on müügil järgmised tooted")
for s in sõn:
    for a in sõn[s]:
        print(f"{s} - {sõn[s][a]}€ ({a})")
        
summa = 0
while True:
    while True:
        soov = str(input("Sisesta ostusoov: "))
        if soov not in sõn and soov != "":
            print("Sellist toodet pole")
        else:
            break
    if soov == "":
        break
        
    värv = str(input("Sisesta toote värvus: "))
    if värv == "":
        break
    leitud = 0
    for asi in sõn:
        for v in sõn[asi]:
            if värv == v:
                summa += sõn[asi][v]
                leitud = 1
                
    if leitud == 0:
        print("Sellise värvusega toodet ei ole")
    else:
        print(f"Jooksev summa on {summa}€")
print(f"tasuda tuleb {summa}€")
                
    