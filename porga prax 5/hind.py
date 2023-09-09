fail = open("hind.txt", encoding="UTF-8")

kokku = 0
kaubad = 0


for rida in fail:
    try:
        kokku += float(rida)
        kaubad += 1
    except:
        kokku += 0
fail.close()

print(f"Ostetud kaupade koguarv on {kaubad}, kogusummaga {kokku}.")