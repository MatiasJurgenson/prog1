#Sisesta poiste pikkused: 180 175 200 172 169 183 188
#Sisesta tüdrukute pikkused: 165 167 172 169 162
#Tantsupaarid on: (185, 172) (182, 170) (178, 169) (175, 164)
#cars = [1, 3, 2] # sain W3 schoolist
#cars.sort(reverse=True)
#print(cars)
#jär = [int(x) for x in jär]

poisid = [int(x) for x in (str(input("Sisesta poiste pikkused: "))).split(" ")] # küsib poiste pikkuseid ja teeb need numbriteks
poisid.sort()

tüdrukud = [int(x) for x in (str(input("Sisesta tüdrukute pikkused: "))).split(" ")] # küsib tüdrulute pikkuseid ja teeb need numbriteks
tüdrukud.sort()

paarid = []
paaritud = []
vahe = (max(len(poisid), len(tüdrukud))) - (min(len(poisid), len(tüdrukud)))
if len(poisid) > len(tüdrukud):
    paaritu = "Poisid"
    for i in range(vahe):
        paaritud.append(poisid[-1])
        poisid.pop(-1)
elif len(poisid) < len(tüdrukud):
    paaritu = "Tüdrukud"
    for i in range(vahe):
        paaritud.append(tüdrukud[-1])
        tüdrukud.pop(-1)
        
    
for i in range(min(len(poisid), len(tüdrukud))):
    paarid.append((poisid[-1-i], tüdrukud[-1-i]))
    
tantsupaarid = ""
for el in paarid:
    tantsupaarid += f" {el}"
    
print(f"Tantsupaarid on:{tantsupaarid}")

paaritudtants = ""
for el in range(len(paaritud)-1):
    paaritudtants += f" {paaritud[el]},"
paaritudtants += f" {paaritud[-1]}"
print(f"{paaritu} pikkustega{paaritudtants} jäid ilma partnerita.") #Lõpeta kodus