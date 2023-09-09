import math

pikkus = float(input("Sisesta ruumi pikkus: "))
laius  = float(input("Sisesta ruumi laius: "))
kõrgus = float(input("Sisesta ruumi kõrgus: "))
maht   = float(input("Sisesta purgi maht: "))

laius_seinad = laius * kõrgus * 2
pikkus_seinad = pikkus * kõrgus * 2

purkide_arv = math.ceil((laius_seinad + pikkus_seinad) / 8 / maht) #ceil sain stackowerfloast
print("Tuleb osta " + str(purkide_arv) + " purki värvi.")