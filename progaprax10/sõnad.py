sõnastik = {}

while True:    
    sõna = str(input("Sisesta sõna: "))
    if sõna == "":
        break
    elif sõna in sõnastik:
        print(f"sõna {sõna} tähendab {sõnastik[sõna]}")
    else:
        print(f"Sõna {sõna} sõnastikus pole")
        tähendus = str(input(f"Mida {sõna} tähendab? "))
        sõnastik[sõna] = tähendus

with open("vasted.txt", "w", encoding="utf-8") as fail:
    for sõne in sõnastik: 
        fail.write(f"{sõne} - {sõnastik[sõne]}\n")
        
print("Sõnastik kirjutati faili.")
print(f"Sõnastikus on {len(sõnastik)} sõna.")