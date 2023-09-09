fail = open("hinnad.txt", encoding="utf-8")
uued_hinnad = []
i = 1
for rida in fail:
    rida = rida.strip("\n")
    if i % 2 == 0:
        try:
            uushind = int(rida) - 0.01
            uued_hinnad.append(toode)
            uued_hinnad.append(uushind)
            print(f"{toode} OK!")
        except:
            print(f"Toote '{toode}' hinda '{rida}' ei õnnestunud teisendada.")
            
    else:
        toode = rida
    i += 1
fail.close()        
uusfail = open("uued_hinnad.txt", "w", encoding = "utf-8")
for asi in uued_hinnad:
    uusfail.write(f"{asi}\n")
    
uusfail.close()
