fail = open("taksohinnad.txt", encoding="utf=8")
andmed = []
for rida in fail:
    rida = rida.strip()
    andmed.append(rida.split(","))
fail.close()
km = float(input("Sisesta tee pikkus kilomeetrites: "))
hinnad = []
for asi in andmed:
    hinnad.append(float(asi[1]) + float(asi[2]) * km)
if andmed == []:
    odavaim = ""
else:
    odavaim = andmed[hinnad.index(min(hinnad))][0]
print(f"Kõige odavam on {odavaim}.")