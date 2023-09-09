def loe_pitsad(a):
    fail = open(a, encoding="UTF-8")
    andmed = []
    for rida in fail:
        rida = rida.strip("\n")
        rida = (rida.split(" "))
        rida[2] = float(rida[2])
        andmed.append(rida)
    fail.close()
    return andmed

def leia_pitsa(a,b):
    for item in a:
        if b == item[0]:
            return item
    return []

#print(leia_pitsa(loe_pitsad("pitsad.txt"), "4"))

def loe_lisandid(a): #peaaegu sama nagu loe_pitsad
    fail = open(a, encoding="UTF-8")
    andmedlisad = []
    andmed = ()
    for rida in fail:
        rida = rida.strip("\n")
        rida = (rida.split(" "))
        rida[2] = float(rida[2])
        
        andmedlisad.append((rida[1], rida[2]))
    fail.close()
    return andmedlisad

#print(loe_lisandid("lisandid.txt"))

def leia_lisand(a,b): # sama nagu pitsa leidmine
    for item in a:
        if b == item[0]:
            return item
    return ('', 0.0)
    
#print(leia_lisand(loe_lisandid("lisandid.txt"), "Sibul"))

tellimus = []
while True:
    pitsatellimus = []
    print("Müügil on järgmised pitsad: ")
    andmedpitsa = loe_pitsad("pitsad.txt")
    pitsalist = ""
    for pitsa in andmedpitsa:
        pitsalist += pitsa[0] + " " + pitsa[1] + " " + str(pitsa[2]) + "; "
    print(pitsalist)


    pitsa = input("Sisesta pitsa ID (lõpetamiseks L): ")
    if pitsa == "L":
        break
        
    if leia_pitsa(andmedpitsa, pitsa) == []:
        print("Sellist pitsat ei ole!")
    else:
        pitsatellimus.append(leia_pitsa(andmedpitsa, pitsa))
        while True:
            lisandid = str(input("Kas soovite lisandeid (jah/ei): "))
            if lisandid == "jah":
                lisandid = loe_lisandid("lisandid.txt")
                lisandidlist = ""
                for lisand in lisandid:
                    lisandidlist += lisand[0] + " " + str(lisand[1]) + "; "
                print(lisandidlist)
                while True:
                    soovib = str(input("Sisesta lisandi nimi: "))
                    if leia_lisand(lisandid, soovib) == ('', 0.0):
                        print("Sellist lisandit ei ole!")
                    else:
                        pitsatellimus.append(leia_lisand(lisandid, soovib))
                        break
            if lisandid == "ei":
                tellimus.append(pitsatellimus)
                break

hind = []
print("Teie tellimus:")
for item in tellimus:
    print(item[0][1] + str(item[0][2]))
    hind.append(item[0][2])
    if len(item) != 1:
        for aine in item:
            print("\t" + aine[0]+ str(aine[1]))#\t sain stackowerflowst
            hind.append(aine[1])
hindl = 0
for asi in hind:
    hindl += asi

#for asi in hind
print("Telimus maksab kokku " + str(hindl) + " eurot.")

fail2 = open("tellimus.txt", mode = "w")
for item in tellimus:
    fail2.write(item[0][1] + str(item[0][2]) + "\n")
    hind.append(item[0][2])
    if len(item) != 1:
        for aine in item:
            fail2.write("\t" + aine[0]+ str(aine[1]) + "\n")#\t sain stackowerflowst
            hind.append(aine[1]
fail2.write("Telimus maksab kokku " + str(hindl) + " eurot." + "\n")
                        
fail2.close()
