import film

def töötleKäsk(käsk, järjend):
    if käsk == "K":
        print("Võimalikud filmid on:")
        võimalikud_filmid = film.loetleFilmid(järjend[0])
        for el in võimalikud_filmid:
            print(el)
        print("")
    
    
    elif käsk == "L":
        filmizanr = järjend[0]
        filminimi = ""
        for i in range(len(järjend)- 1):
            filminimi += f"{järjend[1 + i]} "
        
        film.lisaFilm(filminimi.strip(), filmizanr)
        print("Film lisatud!")
        print("")
        
    elif käsk == "V":
        filminimi = ""
        for el in järjend:
            filminimi += f"{el} "
            
        film.kustutaFilm(filminimi.strip())
        print("""Film nimekirjast kustutatud!
Head vaatamist!""")
        print("")
        
    elif käsk == "E":
        return False


print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")
true = True

while true:
    sisend = str(input(""))
    täht = sisend[0]
    järj = sisend[2:].split(" ")
    true = töötleKäsk(täht, järj)
    if true != False:
        true = True
    
