class Raamat:
    def __init__(self, pealkiri, autor, lehekülgede_arv, liik):
        self.pealkiri = pealkiri
        self.autor = autor
        self.lehekülgede_arv = lehekülgede_arv
        self.liik = liik
        
    def kuva_info(self):
        print(f"{self.pealkiri}, {self.autor}, {self.lehekülgede_arv}, {self.liik}")
        
#tõde_ja_õigus = Raamat("Tõde ja õigus", "A. H. Tammsaare", 453, "romaan")
#tõde_ja_õigus.kuva_info()       
        
class Raamatukogu:
    def __init__(self):
        self.jär = []
            
    def lisa_raamat(self, raamat):
       self.jär.append(raamat)
    
    def kuva_raamatud(self):
        print("Raamatukogus olevad raamatud:")
        [x.kuva_info() for x in self.jär]
        
    def laenuta_raamat(self,raamat):
        for i, raam in enumerate(self.jär):
            if raamat.lower() == raam.pealkiri.lower():
                del self.jär[i]
                return raam
        return None

rk = Raamatukogu()

with open("raamatud.txt", encoding="utf-8") as fail:
    for rida in fail:
        andmed = rida.strip().split(",")
        raamat = Raamat(andmed[0], andmed[1], int(andmed[2]), andmed[3])
        rk.lisa_raamat(raamat)
        
rk.kuva_raamatud()
print("")

while True:
    laenutus = str(input("Sisesta raamatu pealkiri, mida sa laenutada soovid: "))
    laenutatud = rk.laenuta_raamat(laenutus)
    if laenutatud == None:
        print("Ei leidnud sellist raamatut, proovi uuesti!")
    else:
        print("Raamat {laenutatud} edukalt laenutatud!")
        print("")
        break
    
rk.kuva_raamatud()
        
        
    

