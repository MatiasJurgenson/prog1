def riik(frida):
    return frida.split(", ")[0]
#print(riik("Austria, 12, 6, 3, 3, 4, 7, 5, 3, 12, 8, 4, 3"))

def summa(frida1):
    punktid = frida1.split(", ")
    kokku = 0
    for i in punktid[1:]:
        try:
            kokku += int(i.strip(","))
        except:
            pass
 
    return kokku

#print(summa("Itaalia,     2, 12,  4,  6,  3,  5,   ,  5,  8,   ,  5,"))

with open(str(input("Sisesta failinimi: ")), encoding="utf-8") as fail:#punktid.txt
    suurim = 0
    for rida in fail:
        rida = rida.strip()
        if summa(rida) > suurim:
            suurim = summa(rida)
            vriik = riik(rida)
    
    
#print(f"Võitja on {vriik} kogusummaga {suurim} punkti")
    