def seosta_lapsed_ja_vanemad(f1, f2):

    with open(f2, encoding="utf-8") as fnimed, open(f1, encoding="utf-8") as flapsed:
        sõnastiknimed = {}
        numjärjend = []
        for rida in fnimed:
            andmed = rida.strip().split()
            sõnastiknimed[andmed[0]] = f"{andmed[1]} {andmed[2]}"
        for rida in flapsed:
            andmed = rida.strip().split()
            numjärjend.append(andmed)

    nimejärjend = []
    for asi in numjärjend:
        nimed = []
        for i in asi:
            nimed.append(sõnastiknimed[i])
        nimejärjend.append(nimed)
        
    nimekiri = []
    lapsed = []
    
    for vanemlaps in nimejärjend:
        laps = vanemlaps[1]
        lapsed.append(laps)
        vanemad = []
        for vanem in nimejärjend:
            if laps == vanem[1] and laps in lapsed:
                vanemad.append(vanem[0])
        nimekiri.append((laps, vanemad))
    #print(nimekiri)
    
    lõppsõnastik = {}
    for laps in nimekiri:
        lõppsõnastik[laps[0]] = set(laps[1])
    
    return lõppsõnastik
        
        
    #print(nimejärjend)

print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))