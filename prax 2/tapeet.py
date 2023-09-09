import math

print("Sisesta algandmed: ")
print("")

pikkus = float(input("toa pikkus = "))
laius = float(input("toa laius = "))
kõrgus = float(input("toa kõrgus = "))
t_pikkus = float(input("tapeedi pikkus rullis = "))
t_laius = float(input("tapeedi laius rullis = "))

#Elutoa ümbermõõdu ja tapeedi laiuse järgi arvutada toa seinte katmiseks vajaminevate paanide arv.
#Rullis oleva tapeedi pikkuse ja elutoa kõrguse järgi arvutada ühest rullist saadavate paanide arv.
#Paanide koguarvu ja ühes rullis olevate paanide arvu järgi arvutada vajaminevate tapeedirullide arv.

p_arv = math.ceil(((pikkus + laius) * 2) / t_laius)
p_arv_2 = math.floor(t_pikkus / kõrgus)
#p_arv_2 = kõrgus / t_pikkus

kokku = math.ceil(p_arv / p_arv_2)

print("Tuleb osta " + str(kokku) + " rulli tapeeti.")



