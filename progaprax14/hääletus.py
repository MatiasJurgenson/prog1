class Kanditaat:
    def __init__(self, nimi, häälte_arv):
        self.nimi = nimi
        self.häälte_arv = 0
    
    def lisa_hääl(self):
        self.häälte_arv += 1
        
class Valija:
    def __init__(self, nimi):
        self.nimi = nimi
        
    def hääleta(self, kanditaat):
        kanditaat.lisa_hääl()
        
#Jaanus hääletab Kaja poolt
#Urve hääletab Jüri poolt
#Ain hääletab Martini poolt
#Maarja hääletab Kaja poolt
#Siim hääletab Kaja poolt
#Siim hääletab Martini poolt
#Maarja hääletab Jüri poolt
#Jaanus hääletab Jüri poolt
#Ain hääletab Kaja poolt
        
Kaja = Kanditaat("Kaja", 0)
Jüri = Kanditaat("Jüri", 0)
Martin = Kanditaat("Martin", 0)

Jaanus = Valija("Jaanus")
Urve = Valija("Urve")
Ain = Valija("Ain")
Maarja = Valija("Maarja")
Siim = Valija("Siim")

Jaanus.hääleta(Kaja)
Urve.hääleta(Jüri)
Ain.hääleta(Martin)
Maarja.hääleta(Kaja)
Siim.hääleta(Kaja)
Siim.hääleta(Martin)
Maarja.hääleta(Jüri)
Jaanus.hääleta(Jüri)
Ain.hääleta(Kaja)

print(f"{Kaja.nimi} häälte arv on {Kaja.häälte_arv}")
print(f"{Jüri.nimi} häälte arv on {Jüri.häälte_arv}")
print(f"{Martin.nimi} häälte arv on {Martin.häälte_arv}")

print("võitja on Kaja")
