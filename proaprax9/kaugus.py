jär = [int(x) for x in str(input("Sisesta pikkused: ")).split(" ")]
#195 167 165 190 172 182 187 189 168 174
#Inimene nr 8 pikkusega 189 näeb kõige kaugemale.

#[::-1] pöörab listi ümber
kaugeim = 0
kaugele = 0
for i, inim in enumerate(jär):
    try:
        if inim > jär[i+1]:
            j = i
            while j != 0:
                if inim > jär[j]:
                    kaugele += 1
                    j -= 1
                else:
                    kaugeim = kaugele
                    kaugele = 0
                    nr = i + 1
                    kaugeinim = inim
                    j = 0
    except:
        pass

                    
                               
print(f"Inimene nr {nr} pikkusega {kaugeinim} näeb kõige kaugemale")