import math #saadud W3schoolist

suurus = int(input("Milline on pitsa läbimõõt? "))
hind = int(input("Mitu eurot pitsa maksab? "))

#pitsa pindala arvutamine ja hinna jagamine pitsa pindalaga
ruuthind = (hind*100)/(((suurus/2)**2)*math.pi)
print(ruuthind)