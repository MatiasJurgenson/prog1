def failist_sõnastikku(f):
    with open(f, encoding="utf-8") as fail:
        sõnastik = {}
        for rida in fail:
            andmed = rida.strip().split()
            sõnastik[andmed[0]] = andmed[1]
    return sõnastik
            
def koodid_nimedeks(f2, s):
    with open(f2, encoding="utf-8") as fail:
        riigid = []
        for rida in fail:
            rida = rida.strip()
            try:
                riigid.append(s[rida])
                #riigid.append(s.get(rida), 'tundmatu') # kui pole sõnastikus appendib selle asemel 'tundmatu'
            except:
                riigid.append('Tundmatu')
    return riigid
            
sõna = failist_sõnastikku(str(input("Sisesta riigikoodide faili nimi: ")) ) #riigid.txt
jär = koodid_nimedeks(str(input("Sisesta piiriületuste faili nimi: ")), sõna) #piiriületused.txt
for rida in jär:
    print(rida)