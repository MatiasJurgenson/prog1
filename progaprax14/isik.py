class Isik:
    def __init__(self, nimi, vanus, pikkus, kaal):
        self.nimi = nimi
        self.vanus = vanus
        self.pikkus = pikkus
        self.kaal = kaal
        
    def kmi(self):
        return round(self.kaal / ((self.pikkus/100)**2), 1)
    
#isik1 = isik("Anne", 22, 162, 69)
#isik2 = isik("Sirje", 43, 170, 58)

#if isik1.pikkus > isik2.pikkus:
#    print(f"{isik1.nimi} on pikem kui {isik2.nimi}")
#else:
#    print(f"{isik1.nimi} on lühem kui {isik2.nimi}")
    
#if isik1.kaal > isik2.kaal:
#    print(f"{isik1.nimi} kaalub rohkem kui {isik2.nimi}")
#else:
#    print(f"{isik1.nimi} kaalub vähem kui {isik2.nimi}")

jär = []    
with open("tervisekontroll.txt", encoding="utf-8") as fail:
    for rida in fail:
        andmed = rida.strip().split(", ")
        inimene = Isik(andmed[0], int(andmed[1]), int(andmed[2]), int(andmed[3]))
        jär.append(inimene)
        
for inim in jär:
    if inim.kmi() > 25:
        print(f"{inim.nimi}, {inim.vanus}-aastane: sinu kehamassiindeks on {inim.kmi()}, peaksid maha võtma")
    elif inim.kmi() < 19:
        print(f"{inim.nimi}, {inim.vanus}-aastane: sinu kehamassiindeks on {inim.kmi()}, peaksid juurde võtma")
    else:
        print(f"{inim.nimi}, {inim.vanus}-aastane: sinu kehamassiindeks on {inim.kmi()}, oled normaalkaalus")