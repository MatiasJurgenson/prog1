def summa(u, v):
    return (u + v) / (1 + (u * v) / (299792.458**2))

k1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))       #100000
k2 = float(input("Teise keha kiirus esimese keha suhtes on: "))     #150000
k3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))    #200000
k4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: ")) #250000

print("Kiiruste summa on " + str(summa(summa(summa(k1, k2), k3), k4)) + " km/s")