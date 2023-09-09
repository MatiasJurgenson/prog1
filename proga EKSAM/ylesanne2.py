import math
#print(math.pi)
def ruumala(diameeter, kõrgus):
    return math.pi * ((diameeter/2)**2) * kõrgus

def soojusenergia(liik, ruum):
    if liik == "kask":
        return ruum * 1.7
    elif liik == "mänd":
        return ruum * 1.36
    elif liik == "lepp":
        return ruum * 1.23
    else:
        return -1
    
pliik = str(input("Sisesta puuliik: "))
diam = float(input("Sisesta puu diameeter meetrites: "))
kõrg = float(input("Sisesta puu kõrgus meetrites: "))

energia = soojusenergia(pliik, ruumala(diam, kõrg))

if energia == -1:
    print("Sellise puu kohta andmed puuduvad")
else:
    print(f"See puu annab {round(energia, 2)} MWh soojusenergiat.")
    vajaenergia = float(input("Mitu MWh soojusenergiat on vaja? "))
    print(f"{vajaenergia} MWh soojusenergia jaoks on tarvis {math.ceil(vajaenergia/energia)} sellist puud")
    
    



        