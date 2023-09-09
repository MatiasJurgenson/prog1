from random import choice

def mängi(valik1, valik2):
    if valik1 == valik2:
        return "viik"
    elif valik1 == "kivi" and valik2 == "käärid" or valik1 == "käärid" and valik2 == "paber" or valik1 == "paber" and valik2 == "kivi":
        return "esimene"
    else:
        return "teine"
juhuslik = ['kivi', 'paber', 'käärid']    

s = 0
a = 0

for i in range(3):
        arvuti = choice(juhuslik)
        võitja = mängi(str(input("Sisesta oma valik: ")), arvuti)
        if võitja == "esimene":
            s+=1
            nimi = "Sina võitsid!"
        elif võitja == "teine":
            a+=1
            nimi = "Arvuti võitis!"
        else:
            nimi = "Viik!"
        print(f"Arvuti valis {arvuti}. {nimi} Sina {s}, arvuti {a}.")
        
if s > a:
    print("Sina võitsid!")
elif a > s:
    print("Arvuti võitis!")
else:
    print("Mäng jäi viiki!")