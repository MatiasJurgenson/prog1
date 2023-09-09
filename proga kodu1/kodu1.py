def poisse_ja_tüdrukuid(jär):
    poisse = 0
    tüdrukuid = 0
    for element in jär:
        if element[-1] == "P":
            poisse += 1
        elif element[-1] == "T":
            tüdrukuid += 1
    return (poisse, tüdrukuid)

#print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T']))