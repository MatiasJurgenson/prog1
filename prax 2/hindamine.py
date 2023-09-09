while True:
    summa = int(input("Sisesta punktisumma: "))
    if summa >= 0 and summa <= 100:
        break
    else:
        print("Punktisumma peab jääma vahemikku 0–100")
        print("")
while True:
    hindamine = str(input("Kas hindamine on eristav või mitteeristav (e/m)? " ))
    if hindamine == "m" or hindamine == "e":
        break
    else:
        print("Punktisumma peab jääma vahemikku 0–100")
        print("Hindamisviis on tundmatu")
        
if hindamine == "m":
    if summa >= 50:
        print("ARVESTATUD")
    else:
        print("MITTEARVESTATUD")
else:
    if summa >= 90:
        print("A")
    elif summa >= 80:
        print("B")
    elif summa >= 70:
        print("C")
    elif summa >= 60:
        print("D")
    elif summa >= 50:
        print("E")
    else:
        print("F")


#≥90 on A, ≥80 on B, ≥70 on C, ≥60 on D, ≥50 on E ja <50 on F
#Sisesta punktisumma: 95
#Kas hindamine on eristav või mitteeristav (e/m)? m
#ARVESTATUD

#Sisesta punktisumma: -15
#Kas hindamine on eristav või mitteeristav (e/m)? e
#Punktisumma peab jääma vahemikku 0–100

#Sisesta punktisumma: 65
#Kas hindamine on eristav või mitteeristav (e/m)? e
#D

#Sisesta punktisumma: 50
#Kas hindamine on eristav või mitteeristav (e/m)? puudub
#Hindamisviis on tundmatu

