import random

with open("vasted.txt", encoding="utf-8") as fail:
    sõnastik = {}
    for rida in fail:
        väärtused = rida.strip().split(" - ")
        sõnastik[väärtused[0]] = väärtused[1]
i = 0   
while i > -10 and i < 10:
    sõna = random.choice(list(sõnastik))
    vaste = str(input(f" mis on sõna {sõna} vaste? "))
    if sõnastik[sõna] == vaste:
        i+=1
    else:
        i-=1

if i == -10:
    print("Sa surid")
else:
    print("Sa võitsid")
        