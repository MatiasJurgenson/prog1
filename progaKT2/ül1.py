def loe_tulemused(f): #f on sisestatud fail
    with open(f, encoding="utf-8") as fail:
        sõnas = {}
        for rida in fail:
            andmed = rida.strip().split(";")
            punkt = [int(x) for x in andmed[1:]]
            sõnas[andmed[0]] = punkt
    return sõnas

def punktisummad(s):#s on sisestatud sõnasik
    jär = []
    for võti, väärtus in s.items():
        ennik = (võti, sum(väärtus))
        jär.append(ennik)
    return set(jär)
    

sõnastik = loe_tulemused("tulemused.txt")

punktisumma = int(input("Sisestage punktisumma: "))

leidub = 0 #kui ei leidu punktisummat mis on suurem kui sisestatud punktisumma
for element in punktisummad(sõnastik):
    if element[1] > punktisumma:
        print(f"{element[0]} - punktisumma: {element[1]}, punktid 100 meetri distantsilt: {sõnastik[element[0]][0]}")
        leidub = 1
if leidub == 0:
    print("Sellest punktisummast paremat tulemust ei ole")

