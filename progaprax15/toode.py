class Toode:
    def __init__(self, nimi, hind):
        self.nimi = nimi
        self.hind = hind
        
class Boonuskaart:
    def __init__(self):
        self.järjend = []
        
    def lisa_toode(self, toode):
        self.järjend.append(toode)
        
    def arvuta_boonus(self):
        boonus = 0
        for item in self.järjend:
            if toode.hind > >= 10:
                boonus += toode.hind * 0.05
                
        return round(boonus, 2)
    
class Kuldkaart(Boonuskaart):
    def arvuta_boonus(self):
        return round(super().arvuta_boonus() * 1.5 , 2)
    
if str(input("Kas soovid boonuskaarti või kuldkaarti (B/K)? ")) == "B":
    kaart = Boonuskaart()
else:
    kaart = Kuldkaart()
    
while True:
    sisend = str(input("Mida soovid teha: lisa toode, arvuta boonus, välju (L/A/V)? "))
    if sisend == "V":
        break
    elif sisend == "L":
        print("Sisesta toote nimi: Pintsel")
        print("Sisesta toote hind: 17.49")