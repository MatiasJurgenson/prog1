def eelarve(x):
    return  x*10+55


#vähim = int(input("Sisesta vähim külaliste arv: "))#15
#suurim = int(input("Sisesta suurim külaliste arv: "))#26
#print(f"Peo eelarve jääb vahemikku {eelarve(vähim)} kuni {eelarve(suurim)} eurot.")

sümbolid = ["-", "+", "?"]
kutsutud = 0
vähim = 0
suurim = 0

fail = str(input("Sisesta failinimi: "))#pidu.txt

fail = open(fail, encoding="UTF-8")
for rida in fail:
    rida = rida.strip("\n")
    if rida not in sümbolid:
        kutsutud += 1
    else:
        if rida == sümbolid[1]:
            vähim += 1
            suurim += 1
        elif rida == sümbolid[2]:
            suurim += 1
                
fail.close()                
                
            

print(f"Kokku on kutsutud {kutsutud} inimest")
print(f"Vähim võimalik osavõtjate arv on {vähim}")
print(f"Suurim võimalik osavõtjate arv on {suurim}")
print(f"Peo vähim võimalik eelarve on {eelarve(vähim)} eurot")
print(f"Peo suurim võimalik eelarve on {eelarve(suurim)} eurot")