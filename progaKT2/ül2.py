def leia_keskmised(f):
    jär = []
    with open(f, encoding="utf-8") as fail:
        for rida in fail:
            andmed = rida.strip().split()
            arvud = [int(x) for x in andmed]
            keskmine = round((sum(arvud) / len(arvud)),2)
            jär.append(keskmine)
    return jär

def kas_rohkem_väravaid(j,oot):#j on järjend, oot on oodatavate väravate arv
    hooajakeskmine = oot/38
    for arv in j:
        if arv < hooajakeskmine:
            return False
    return True

sisfail = str(input("Sisesta faili nimi: "))
väravad = int(input("Sisesta, kui palju väravaid peaks lööma? "))

järjend = leia_keskmised(sisfail)

print("Jalgpallurite keskmised on:")
for kesk in järjend:
    print(kesk)
    
if kas_rohkem_väravaid(järjend, väravad): #kui väljund on True siis
    print("Kõik mängijad löövad tõenäoliselt piisavalt väravaid.")
else:
    print("Kõik mängijad ei löö tõenaoliselt piisavalt väravaid.")
    
