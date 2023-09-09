import random
import matplotlib.pyplot as plt # sain thonnys tööle aga pidin läbi vscode tõmbaba sest thonny plugin installer brokey


x = random.randint(0, 10)
y = random.randint(0, 10)
#print(x, y)

pakkumiste_arv = 0
pakkumised = []
while True:
    
    pakkumine = str(input("Sisesta pakkunime: "))
    pakkumiste_arv += 1
    xy = pakkumine.split(" ")
    xy = [int(arv) for arv in xy]
    pakkumised.append((xy[0], xy[1]))
    
    if x == xy[0] and y == xy[1]:
        
        print("pakkusite õigesti")
        print(f"punkti leidmiseks kulus {pakkumiste_arv} pakkumist")
        break
    
    else:
        kaugus = ((x - xy[0])**2 + (y - xy[1])**2)**(1/2)
        print(f"kaugus punktist on {kaugus}")
        print("")

#print(pakkumised)
pakkumised_x = [x for x, y in pakkumised]
pakkumised_y = [y for x, y in pakkumised]
        
plt.plot(pakkumised_x, pakkumised_y)
plt.ylabel('some numbers')
plt.show()