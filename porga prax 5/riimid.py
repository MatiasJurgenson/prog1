algne = str(input("Sisesta algne sõna: "))
riimudearv = []
riimudsõnad = []
while True:
    riimuv = str(input("Sisesta riimuv sõna: "))
    i = -1
    riimuarv = 0
    if riimuv == "lõpp":
        break
    else:
        for täht in riimuv:
            try:
                if algne[i] == riimuv[i]:
                    riimuarv += 1
                    i -= 1
                else:
                    i = 100
                    riimudearv.append(riimuarv)
                    print(f"Riimumisnäitaja on {riimuarv}")
                    riimudsõnad.append(riimuv)
            except:
                continue
#riimudearv.index(max(riimudearv))        
print(f"Kõige suurem riimumisnäitaja {max(riimudearv)} oli sõnal '{riimudsõnad[riimudearv.index(max(riimudearv))]}'.")     
                