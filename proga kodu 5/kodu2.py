import string
import random

def suurväike(x):
    märgid = string.punctuation
    vahetatud = x.swapcase()
    märgidvahetavad = []
    for märk in vahetatud:
        if märk in märgid and märk != märgidvahetavad:
            b = random.choice(märgid)
            vahetatud = vahetatud.replace(märk, b)
            märgid = märgid.replace(b, "")

    
    return vahetatud

f = str(input("Sisesta faili nimi: "))
fail = open(f, encoding="UTF-8")
for rida in fail:
    rida = rida.strip("\n")
    print(suurväike(rida))
    
fail.close()
    
