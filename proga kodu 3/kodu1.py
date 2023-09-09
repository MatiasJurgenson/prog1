import math

def koogi_hind(nimi, mõõt):
    if nimi == "Napoleoni kook":
        hind = mõõt**2*0.08
    elif nimi == 'šokolaadikook':
        hind = mõõt**2*math.pi*0.05
    elif nimi == 'ploomikook':
        hind = mõõt**2*math.pi*0.04
    else:
        return -1
    return round(hind, 2)

a = str(input("Sisesta koogi nimi: "))
b = float(input("Sisesta koogi mõõt: "))

if koogi_hind(a, b) == -1:
    print("Sellist kooki pagarikoda ei valmista.")
else:
    print("Selle koogi hind on " + str(koogi_hind(a, b)) + " eurot.")