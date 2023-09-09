def kirja_hind(x):
    if x <= 250:
        return 1.75
    elif x > 250 and x <= 500:
        return 2.70
    elif x > 500 and x <= 1000:
            return 2.85
    else:
        return 4.35
    
kirjad = int(input("Sisesta kirjade arv: "))
i = 0
hind = 0
while i < kirjad:
    kulu = int(input("Sisesta " + str(i + 1) + ". kirja kaal: "))
    hind += kirja_hind(kulu)
    i += 1
print("Nende kirjade saatmine läheb maksma " + str(hind) + " eurot.")