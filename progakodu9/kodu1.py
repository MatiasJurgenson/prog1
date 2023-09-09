def failist_järjendisse(sisend):
    with open(sisend, encoding="utf-8") as fail:
        retseptid = []
        for rida in fail:
            retsept = rida.strip().split(",")
            retseptid.append(retsept)
    return retseptid
            
            
maasjasuh = []           
for retsept in failist_järjendisse("retseptid.txt"):
    if "suhkur" in retsept and "maasikad" in retsept:
        maasjasuh.append(retsept)
        
print("Retseptid, milleks on vaja maasikaid ja suhkrut:")

for i in maasjasuh:
    s=""
    for item in range(len(i)-1):
        s += f"{i[item]}, "
    s+= i[-1]
    print(s)
