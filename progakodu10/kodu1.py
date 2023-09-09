def erinevad_sümbolid(sõne):
    return set(sõne)

#print(erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente"))

def sümbolite_sagedus(sõne):
    hulk = erinevad_sümbolid(sõne)
    sõnastik = {}
    for el in hulk:
        i = 0
        for täht in sõne:
            if täht == el:
                i += 1
        sõnastik[el] = i
    return sõnastik
        
#print(sümbolite_sagedus("Hei hopsti, väikevend!"))

def grupeeri(sõne):
    täishäälikudtähed = ['a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü'] # saadud miksike.ee
    kaashäälikudtähed = ['b', 'd', 'c', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'Ž', 't', 'v', 'w', 'x', 'y']
    sõnastik = sümbolite_sagedus(sõne)
    
    thulk = set()
    khulk = set()
    mhulk = set()
    
    for el in sõnastik:
        if el.lower() in täishäälikudtähed:
            thulk.add((el, sõnastik[el]))
        elif el.lower() in kaashäälikudtähed:
            khulk.add((el, sõnastik[el]))
        else:
            mhulk.add((el, sõnastik[el]))
    
    return {'Täishäälikud': thulk, 'Kaashäälikud': khulk, 'Muud': mhulk}
            
        
#print(grupeeri("sõida tasa üle silla"))
            
    
        