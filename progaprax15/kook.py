import math

class Kook:
    def __init__(self, nimi, mõõt, hind):
        self.nimi = nimi
        self.mõõt = mõõt
        self.hind = hind
        
    def pindala(self):
        return self.mõõt**2
    
    def cm2hind(self):
        return round(self.hind * 100 / self.pindala(), 2)
    
class Ümarkook(Kook):
    #def __init__(self): ülemklassis juba konstruktor olemas
    
    def pindala(self):
        return (self.mõõt/2)**2 * math.pi
    
class Pitsa(Ümarkook):
    def __init__(self, nimi, mõõt, hind, kate):
        super().__init__(nimi, mõõt, hind)
        self.kate = kate
    
    def cm2hind(self):
        return round((self.hind + self.kate) * 100 / self.pindala(), 2)
    
    
k1 = Kook("Mustikakook", 8, 3.52)
k2 = Ümarkook("Porgandi-kõrvitsa pitsapõhi", 24, 1.85)
k3 = Pitsa("Caesari pitsa", 24, 1.85, 6.70)

jär = [k1, k2, k3]
väikseim = None
for arv, kook in enumerate(jär):
    if väikseim == None or kook.cm2hind() < väikseim.cm2hind():
        väikseim = kook
        
print(väikseim.nimi, väikseim.cm2hind())
        
    
    
    