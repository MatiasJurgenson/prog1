def loe_andmed(fail):
    jär = []
    with open(fail, encoding="utf-8") as f:
        for rida in f:
            müüa = []
            rida = rida.strip().split(";")
            raamatud = [int(x) for x in rida[1:]]
            müüa.append(rida[0])
            müüa.extend(raamatud)
            jär.append(müüa)
    return jär

#print(loe_andmed("müügid.txt"))

def parim_töötaja(järjend, kuu):
    suurim = 0
    for töötaja in järjend:
        if töötaja[kuu] > suurim:
            suurim = töötaja[kuu]
            töö = töötaja[0]
    return töö

print(parim_töötaja(loe_andmed("müügid.txt"), 1))
        
        