lohed = int(input("Sisesta lohede arv: "))#3
maod = int(input("Sisesta madude arv: "))# 5
saurused = int(input("Sisesta sauruste arv: "))# 9
#Viimane söögikord toimus 5. päeval
#Järele jäi 2 madu
söök = 0
järel = []
while järel.count(0) != 2: #counti sain proga õpikust
    if maod > 0 and lohed > 0:
        maod -= lohed
    if saurused > 0 and maod > 0:
        saurused -= maod
    if lohed > 0 and saurused > 0:
        lohed -= saurused
    söök += 1
    if maod < 0: #kui mingi loom on otsas ja negatiivne teeb ta selle 0ks
        maod = 0
    if lohed < 0:
        lohed = 0
    if saurused < 0:
        saurused = 0
        
    
    järel = [lohed, maod, saurused]
print(f"Viimane söögikord toimus {söök} päeval")
if maod != 0:
    print(f"Järele jäi {järel[1]} madu")
if lohed != 0:
    print(f"Järele jäi {järel[0]} lohet")
if saurused != 0:
    print(f"Järele jäi {järel[2]} saurust")


    