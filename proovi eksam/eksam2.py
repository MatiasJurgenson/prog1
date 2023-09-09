class Õun:
    def __init__(self, nimi, värv):
        self.nimi = nimi
        self.värv = värv
        
    def muuda_värvi(self, uus_värv):
        self.värv = uus_värv
        
    def kilohind(self):
        if self.värv == 'roheline':
            return 0.79
        elif self.värv == 'kollane':
            return 1.89
        elif self.värv == 'punane':
            return 2.49
        
    def __str__(self):
        return(f"Õun {self.nimi}, {self.värv}, kilohind {self.kilohind()}")
    
class Kuldrenett(Õun):
    def __init__(self, värv, suurus):
        nimi = 'Kuldrenett'
        self.värv = värv
        super().__init__(nimi, värv)
        self.suurus = suurus
        
    def kilohind(self):
        return round(self.suurus*0.55, 2)
    
"""
Põhiprogrammis:

loo klassi Õun isend, mille puhul nimi on Suislepp ja värv roheline;
väljasta selle õuna kilohind;
muuda õuna värv rohelisest punaseks;
väljasta uuesti kilohind;
loo klassi Kuldrenett isend, võttes värviks kollane ja suuruseks 6,5;
väljasta selle isendi kirjeldus, nagu meetod __str__ selle tagastab.
Väljundi näide

Õuna kilohind on 0.79
Värv muutub...
Õuna kilohind on 2.49
Õun 'Kuldrenett', kollane, kilohind 3.58
"""

suislepp = Õun("Suislepp", "roheline")
print("Õuna kilohind on", suislepp.kilohind())
suislepp.muuda_värvi("punane")
print("Värv muutub...")
print("Õuna kilohind on", suislepp.kilohind())

kuldrenett = Kuldrenett("kollane", 6.5)
print(kuldrenett)

        