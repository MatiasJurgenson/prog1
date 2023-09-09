def arvuta_tasu(tund, määr):
    ületund = 0
    tavatund = 40
    if tavatund > tund:
        tavatund = tund
    if tund > 40:
        ületund = tund - 40
    #40*10 + 5*1.5*10 = 475.0
    return tavatund*määr + ületund*1.5*määr

töötaja1 = str(input("Sisesta 1. töötaja nimi: ")) #Utos
töötaja1tund = float(input("Sisesta 1. töötaja tunnid: ")) #20
töötaja1määr = float(input("Sisesta 1. töötaja tasumäär: ")) #25
töötaja2 = str(input("Sisesta 2. töötaja nimi: ")) #Rork
töötaja2tund = float(input("Sisesta 2. töötaja tunnid: ")) #45
töötaja2määr = float(input("Sisesta 2. töötaja tasumäär: ")) #10
#Utos saab suuremat tasu kui Rork

if arvuta_tasu(töötaja1tund, töötaja1määr) > arvuta_tasu(töötaja2tund, töötaja2määr):
    print(töötaja1 + " saab suuremat tasu kui " + töötaja2)
else:
    print(töötaja2 + " saab suuremat tasu kui " + töötaja1)
    
