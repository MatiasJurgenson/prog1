import random

class Draakon:
    def __init__(self, nimi):
        self.nimi = nimi
        
    def ründa(self):
        print(self.nimi, "möirgab")
        
class Maadraakon(Draakon):
    def __init__(self, nimi, energia):
        super().__init__(nimi)
        self.energia = energia
        
    def ründa(self):
        if self.energia > 0:
            print(self.nimi, "väristab maad")
            self.energia -= 1
            
        else:
            super().ründa()
    
class Tuledraakon(Draakon):
    def __init__(self, nimi, kütus):
        super().__init__(nimi)
        self.kütus = kütus
        
    def ründa(self):
        if self.kütus >= 10:
            print(self.nimi, "sülgab tuld")
            self.kütus -= 10
            
        else:
            super().ründa()
            
class Kividraakon(Maadraakon):
     def __init__(self, nimi, energia, kivid):
        super().__init__(nimi, energia)
        self.kivid = kivid
        
     def ründa(self):
        if self.kivid > 0:
            if self.kivid >= 3:
                print(self.nimi, "heidab 3 kivi")
                self.kivid -= 3
            else:
                print(self.nimi, f"heidab {self.kivid} kivi")
                self.kivid = 0
        else:
           super().ründa()
           
class Laavadraakon(Tuledraakon):
    def __init__(self, nimi, kütus, laava):
        super().__init__(nimi, kütus)
        self.laava = laava
    
    def ründa(self):
        laava_kogus = random.randint(1, min(100, self.laava))
            
        if self.laava > laava_kogus:
            print(self.nimi, f"paiskab {laava_kogus} laavat")
            self.laava -= laava_kogus
        
        else: 
            super().ründa()
                
    
        
veldora = Draakon("Veldora")
veldora.ründa()
print("")

chiki = Maadraakon("Chiki", 4)
chiki.ründa()
print("")

rytys = Tuledraakon("Rytys", 30)
rytys.ründa()
print("")

kivike = Kividraakon("kivike", 1, 2)
kivike.ründa()
kivike.ründa()
kivike.ründa()

print("")
lava = Laavadraakon("Lava", 10, 200)
for i in range(10):
    lava.ründa()