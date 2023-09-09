def failist_järjendisse(sisend):
    with open(sisend, encoding="utf-8") as fail:
        bingo = []
        for rida in fail:
            rida = [int(x) for x in rida.strip().split(" ") ]
            bingo.append(rida)
    return bingo
#print(failist_järjendisse("bingo.txt"))

def on_bingo_tabel(tabel):
    for i in tabel:
        number = 15
        for j in i:
            if j >= number - 14 and j <= number:
                number += 15
            else:
                return False
    return True

#print(on_bingo_tabel(failist_järjendisse("bingo.txt")))               