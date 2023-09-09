from urllib.request import urlopen

def loe_saladus(url, algus, lõpp):
    try:
        allikas = urlopen(url)
        baidid = allikas.read()
        tekst = baidid.decode()
        sala_algus = tekst.index(algus) + len(algus)
        return tekst[sala_algus:tekst.index(lõpp)]
    except:
        return ""
    
    
#x = "s4ladus:"
#y = ":s4ladus"

#loe_saladus("https://courses.cs.ut.ee/2022/programmeerimine/fall/Main/Kodu5", x, y)
