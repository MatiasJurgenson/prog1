def loetleFilmid(zanr):
    filmid = []
    with open("filmid.txt", encoding = "utf-8") as filmifail:
        for rida in filmifail:
            rida = rida.strip()
            filmid.append(rida.split(" - "))
        
    zanrfilmid = []
    for film in filmid:
        if film[1] == zanr:
            zanrfilmid.append(film[0])
    return zanrfilmid

#print(loetleFilmid("märul"))

def lisaFilm(nimi, zanr):
    with open("filmid.txt", "a+",encoding = "utf-8") as filmifail:
        filmifail.write(f"\n{nimi} - {zanr}")
        
#lisaFilm("nimi", "zanr")
        
def kustutaFilm(mittefilm):
    filmid = []
    with open("filmid.txt", encoding = "utf-8") as filmifail:
        for rida in filmifail:
            rida = rida.strip()
            if rida != "":
                filmid.append(rida.split(" - "))
    with open("filmid.txt", "w",encoding = "utf-8") as filmifail:
        for film in filmid:
            if film[0] != mittefilm:
                filmifail.write(f"{film[0]} - {film[1]}\n")
                
#kustutaFilm("Shrek")
            
        
