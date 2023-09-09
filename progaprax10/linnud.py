def linnud_sõnastikku(f):
    sõnastik = {}
    with open(f, encoding="utf-8") as fail:
        for rida in fail:
            jär = rida.strip().split(",")
            sõnastik[jär[0]] = int(jär[1])
    return sõnastik


sõnastiklinnud = linnud_sõnastikku(str(input("Sisesta failinimi: ")))

arv = int(input("Sisesta arv: "))

i=0

for x, y in sõnastiklinnud.items():
    if int(y) > arv:
        print(f"{x} ({y})")
    i+=y

print(f"Juku nägi väljas {i} lindu.")
        