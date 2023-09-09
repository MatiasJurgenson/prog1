import random

class Lotopilet:
    def __init__(self):
        self.hind = 1.5
        self.põhinumbrid = []
        self.lisanumbrid = []
        
    def __str__(self):
        return f"Pileti hind: {self.hind}\nPileti põhinumbrid: {self.põhinumbrid}\nPileti lisanumbrid: {self.lisanumbrid}"

class Eurojackpot(Lotopilet):
    def pliksplaks(self):
        põhi_arvud = random.sample(range(1, 51), k=5)
        lisa_arvud = random.sample(range(1, 13), k=2)
        
        self.põhinumbrid.extend(põhi_arvud)
        self.lisanumbrid.extend(lisa_arvud)

pilet = Eurojackpot()
pilet.pliksplaks()
print(pilet)