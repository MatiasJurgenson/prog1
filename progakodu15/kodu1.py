#sõiduki mark, sõiduki hind eurodes ja sõiduki kütusekulu 100 kilomeetri
class Sõiduk:
    def __init__(self, mark, hind, kulu):
        self.mark = mark
        self.hind = hind
        self.kulu = kulu
        
    def __str__(self):
        return f"{self.mark}, hind {self.hind} eurot, kütusekulu 100 km kohta {self.kulu} liitrit."
    
class Veoauto(Sõiduk):
    def __init__(self, mark, hind, kulu):
        self.mark = mark
        self.hind = hind
        self.kulu = kulu
        self.liiter = 1.8
        self.hobesejõud = 500
        
    def sõidu_maksumus(self, teepikkus):
        return round(teepikkus / 100 * self.kulu * self.liiter, 1)
    
    def hobujõud(self):
        print(f"Veoautol on {self.hobesejõud} hobujõudu.")
    
class Sõiduauto(Sõiduk):
    def __init__(self, mark, hind, kulu):
        self.mark = mark
        self.hind = hind
        self.kulu = kulu
        self.liiter = 1.9
        self.hobesejõud = 180
        
    def sõidu_maksumus(self, teepikkus):
        return round(teepikkus / 100 * self.kulu * self.liiter, 1)
    
    def hobujõud(self):
        print(f"Sõiduautol on {self.hobesejõud} hobujõudu.")

class Mootorratas(Sõiduk):
    def __init__(self, mark, hind, kulu):
        self.mark = mark
        self.hind = hind
        self.kulu = kulu
        self.liiter = 1.85
        self.hobesejõud = 85
        
    def sõidu_maksumus(self, teepikkus):
        return round(teepikkus / 100 * self.kulu * self.liiter, 1)
    
    def hobujõud(self):
        print(f"Mootorrattal on {self.hobesejõud} hobujõudu.")
        
class Garaaž:
    def __init__(self, järjend):
        self.järjend = järjend
        
    def kuva(self):
        for sõiduk in self.järjend:
            print("")
            print(sõiduk)
            sõiduk.hobujõud()
            print(f"Tartu-Tallinna vahemaa läbimiseks kulub {sõiduk.sõidu_maksumus(186)} eurot.")
    
sõidukite_jär = []
with open("sõidukid.txt", encoding="utf-8") as fail:
    for rida in fail:
        andmed = rida.strip().split(" - ")
        andmed_sõiduk = andmed[1].split(", ")
        if andmed[0] == "Veoauto":
            sõiduk = Veoauto(andmed_sõiduk[0], int(andmed_sõiduk[1]), float(andmed_sõiduk[2]))
            sõidukite_jär.append(sõiduk)
        elif andmed[0] == "Sõiduauto":
            sõiduk = Sõiduauto(andmed_sõiduk[0], int(andmed_sõiduk[1]), float(andmed_sõiduk[2]))
            sõidukite_jär.append(sõiduk)
        elif andmed[0] == "Mootorratas":
            sõiduk = Mootorratas(andmed_sõiduk[0], int(andmed_sõiduk[1]), float(andmed_sõiduk[2]))
            sõidukite_jär.append(sõiduk)

garaaz = Garaaž(sõidukite_jär)

print("Garaažis on järgmised sõidukid:")
garaaz.kuva()
            
            
        
            