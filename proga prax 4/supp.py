
supp = int(input("Sisesta supi algtemperatuur: "))
ruum = int(input("Sisesta ruumi temperatuur: "))

while supp > ruum and round(supp, 6) != ruum:
    supp = supp - (supp - ruum)*0.19
    print("Supi temperatuur on "+ str(supp))