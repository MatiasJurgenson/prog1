kuu = int(input("Sisesta kuu number: "))
 
if kuu == 12:
    print("talv")
else:
    if kuu == 1 or kuu == 2:
        print("talv")
    else:
        if kuu >= 3 and kuu <= 5:
            print("kevad")
        elif kuu >= 6 and kuu <= 8:
            print("suvi")
            ... # ee, ei oska siia midagi kirjutada, pea juba valutab
        else:
            print("sügis")