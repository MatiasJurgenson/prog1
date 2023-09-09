f = str(input("Palun sisestage failinimi: "))

def a(arv1):
    return 1
def b(arv2):
    return 2
a(1)
b(2)

#spagett
with open(f, encoding="utf-8") as fail:
    read = fail.readlines()
    #print(read)
    main_jär = []
    kohtade_jär = []
    klassi_jär = []
    for rida in read:
        
        klass1, kohad = rida.strip().split()
        kohtade_jär.append(kohad)
        klassi_jär.append(klass1)
    main_jär.append(kohtade_jär)
    

sõnastik = {}
    
for index2, klass2 in enumerate(klassi_jär):
    jär = []
    for index3, klass3 in enumerate(klassi_jär):
        if klass2 == klass3:
            jär.append(index3)
    sõnastik[klass2] = set(jär)
    
main_jär.append(sõnastik)
#print(main_jär)
        
        
        
klass = str(input("Mis klassist olete? "))
piletid = int(input("Mitu piletit soovite? "))

blank = []
uusrida = ''
try:
    for klassirida in main_jär[1][klass]:
        for i in range(len(main_jär[0][klassirida])- piletid +1):
            if main_jär[0][klassirida][i:i+piletid] == '-'*piletid:
                uusrida += klass
                for koht in range(piletid):
                    s = f"(rida {klassirida + 1}, koht {i + 1 + koht})"
                    blank.append(s)
                    main_jär[0][klassirida] = main_jär[0][klassirida].replace("-"*piletid, "x"*piletid, 1)
                uusrida += f" {main_jär[0][klassirida]}\n"
                #print(uusrida)
                #print(klassirida)
                
                print(f"Teie kohad on {blank[0]}", end='')
                for koht1 in blank[1:]:
                    print(",",koht1)
                    
                read[klassirida]=uusrida

                            
                with open(f, "w", encoding="utf-8") as fail1:
                    for rida1 in read:
                        #print(rida1)
                        fail1.write(rida1)
                    
                    
                         
        else:
            continue
        break

    if blank == []:
        print("Palun vabandust, aga sobivaid kohti ei ole")
        
except:
    print("Palun vabandust, aga sobivaid kohti ei ole")
            
            

    