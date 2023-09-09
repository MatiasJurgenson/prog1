import string
import random



def suurväike(x):
    märgid = string.punctuation
    vahetatud = x.swapcase()
    b = random.choice(märgid)
    for märk in vahetatud:
        if märk in märgid:
            vahetatud = vahetatud.replace(märk, b)
            märgid = märgid.replace(b, "")

    
    return vahetatud
    
a = str(input(""))
print(suurväike(a))