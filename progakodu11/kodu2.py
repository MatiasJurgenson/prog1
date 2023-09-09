def loe_failist(fail):
    sõnastik = {}
    with open(fail, encoding="utf-8") as f:
        for rida in f:
            andmed = rida.strip().split(";")
            punktid = [int(x) for x in andmed[1:]]
            sõnastik[andmed[0]] = punktid
    return sõnastik
            
def leia_keskmine(s):
    summa = 0
    for y in list(s.values()):
        summa += sum(y) / len(y)
    summa /= len(s)
        
    
    return round(summa, 1)
        
sõnas = loe_failist(str(input("Sisesta failinimi: ")))#tulemused.txt
print("Voorude keskmised tulemused on:")
for x in list(sõnas.values()):
    print(round((sum(x) / len(x)), 1)) # 3.5 4.0 6.8

print(f"Kõikide voorude keskmine tulemus on: {leia_keskmine(sõnas)}")   