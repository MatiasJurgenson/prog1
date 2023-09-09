fail = str(input("Sisesta faili nimi: "))
uusfail = open("raha.txt", "w", encoding="utf-8")

eiostmine = str(input("Mida poest mitte osta: "))

fail = open(fail, encoding="utf-8")
kokku = 0
tooted = []
i= 0
for rida in fail:
    rida = rida.strip("\n")
    if i != 0: # toote mida ei vajata ridadest mõõdumine
        i -= 1
        continue
    if rida != eiostmine:
        
        try:
            ostekokku = int(rida)
            kokku += hind * ostekokku
        except:
            try:
                hind = float(rida)
            except:
                tooted.append(rida)
    else:
       i = 2 
fail.close()
nimekiri = "Ostunimekiri: "
for toode in tooted:
    nimekiri += f"{toode} "
print(nimekiri)
raha = 15 - kokku
print(f"Ostu maksumus on {kokku} eurot.")
if raha > 0:
    print("Pillel jätkus raha poes käimiseks!")
    uusfail.write(f"Pillel jäi raha üle {round(raha, 2)} eurot.")
else:
    print("Pillel ei jätkunud raha poes käimiseks!")
    uusfail.write(f"Pillel tuli raha puudu {-1 * round(raha, 2)} eurot.")
uusfail.close()
    
