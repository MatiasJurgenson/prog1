with open("sünnid.txt", encoding="utf=8") as fsünnid, open("surmad.txt", encoding="utf=8") as fsurmad:
    sünnid = [x.strip() for x in fsünnid.readlines()]
    surmad = [x.strip() for x in fsurmad.readlines()]
    iive = []
    kuud = []
    for i in range(len(sünnid)):
        if i % 2 == 0:
            kuud.append(sünnid[i])
            
        else:
            iive.append(int(sünnid[i]) - int(surmad[i]))
            
print("Positiivse iibega kuud olid:")
for i in range(len(kuud)):
    if iive[i] > 0:
        print(f"{kuud[i]} {iive[i]}")
print(f"Kogu ajavahemiku loomulik iive oli {sum(iive)}")
        
    