a = ['19.04', '21.05', '04.07', '21.05', '11.11', '12.03', '04.07', '08.06', '12.03', '21.05', '12.03']

sõnastik = {}
kontrollitud = []
for el in a:
    if el not in kontrollitud:
        kontrollitud.append(a)
        i = a.count(el)
        sõnastik[el] = i
        
for x, y in sõnastik.items():
    if y == max(list(sõnastik.values())):
        print(x)
    
    
    
        
    

    