def loe_andmed(f):
    with open(f, encoding="utf-8") as fail:
        
        #võtsin inspiratsiooniks näidiseksami ül-i lahenduse
        nime_jär = []
        unikaalsed_nimed = []
        sordi_jär = []
        koguse_jär = []
        
        for rida in fail:
            nimi, sort, kogus = rida.strip().split(";")
            nime_jär.append(nimi)
            sordi_jär.append(sort)
            koguse_jär.append(float(kogus))
            if nimi not in unikaalsed_nimed:
                unikaalsed_nimed.append(nimi)
                
    sõnastik = {}
            
    for nimi1 in unikaalsed_nimed:
        sort_kogus = []
        for arv, nimi2 in enumerate(nime_jär):
            if nimi1 == nimi2:
                sort_kogus.append((sordi_jär[arv], koguse_jär[arv]))
        sõnastik[nimi1] = sort_kogus
            
    return sõnastik

def lisa_tellimus(sõn):
    while True:
        tellija = str(input("Tellija nimi: "))
        kommid = ('karamell', 'šokolaad', 'martsipan', 'pralinee', 'marmelaad')
        komm = str(input(f"Kommid {kommid}: "))
        if komm in kommid:
            break
        else:
            print("Sellist kommi ei ole")
    kogus = float(input("Tellitav kogus: "))
    
    komm_järjendis = 0
    
    if tellija in sõn:
        for index, komm_tellimus in enumerate(sõn[tellija]):
            if komm_tellimus[0] == komm:
                sõn[tellija][index] = (komm, sõn[tellija][index][1] + kogus)
                komm_järjendis = 1
                break
            
        if komm_järjendis == 0:
            lisatav = (komm, kogus)
            sõn[tellija].append(lisatav)
    
    else:
        sõn[tellija] = [(komm, kogus)]
       
    return sõn
            
# kui kogus >= 2 hind alla 10%
def arvuta_hind(sort, kogus):
    if sort == 'karamell' or sort == 'martsipan':
        hind = kogus*15
    else:
        hind = kogus*10
        
    if kogus >= 2:
        return hind*0.9
    else: return hind
    
def vormista_tellimus(sõnastik):
    while True:
        tellija = str(input("Tellija nimi: "))
        if tellija in sõnastik:
            break
        else:
            print("Sellist tellijat ei ole")
            
    summa = 0
    for tellimus in sõnastik[tellija]:
        summa += arvuta_hind(tellimus[0], tellimus[1])
        
    print(f"{tellija} tellimuse kogusumma: {summa} eurot.")
    del sõnastik[tellija]
    
    return sõnastik
    
def sõnastik_faili(sõnastik, f):
    with open(f, 'w', encoding='utf-8') as fail:
        for tellija in sõnastik:
            for tellimus in sõnastik[tellija]:
                fail.write(f"{tellija};{tellimus[0]};{tellimus[1]}\n")
                

#print(loe_andmed("kommid.txt"))
#print(lisa_tellimus(loe_andmed("kommid.txt")))
#print(arvuta_hind('pralinee', 1))
#print(vormista_tellimus(loe_andmed("kommid.txt")))
#sõnastik_faili(loe_andmed("kommid.txt"), "kommid_uus.txt")

main_sõnastik = loe_andmed("kommid.txt")
print("1 - Lisa tellimus\n2 - Vormista tellimus\n3 - Lõpeta töö")
                
while True:
    tegevus = int(input("Vali tegevus: "))
    if tegevus == 1:
        main_sõnastik = lisa_tellimus(main_sõnastik)
        
    elif tegevus == 2:
        main_sõnastik = vormista_tellimus(main_sõnastik)
        
    elif tegevus == 3:
        sõnastik_faili(main_sõnastik, "kommid_uus.txt")   
        print("Tellimused kirutatud faili kommid_uus.txt")
        break
    
    else:
        print("Sellist tegevust pole")

            

                 
            
            