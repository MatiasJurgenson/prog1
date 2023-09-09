def loe_tulemused(f): 
    with open(f, encoding = "utf-8") as fail:
        nimekiri = []
        for rida in fail:   
            rida = rida.strip().split(";")
            nimekiri.append(rida)
    return nimekiri
            
#print(loe_tulemused('hokiturniir.txt'))

def kes_võitis(jär):
    suurimV = 0
    võistkond = 0
    
    for i, y in enumerate(jär):
        prarguneV = 0
        for v in y:
            if v == "V":
                prarguneV += 1
        if prarguneV > suurimV:
            suurimV = prarguneV
            võistkond = i+1
    return võistkond
print(f"Turniiri võitis {kes_võitis(loe_tulemused(str(input('Sisestage failinimi: '))))}. võistkond.")

    
            