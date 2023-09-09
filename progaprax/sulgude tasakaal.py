#Sisesta sõne: suured (õieti tohutud) lained
#Sulud on tasakaalus 

#Sisesta sõne: {[(])} [()]{}{[()()]()} (()()))()((())
#Sulud ei ole tasakaalus
tase = 0
suludV = ["(","[","{"]
suludP = [")","]","}"]
tasemesulud = []
tasakaalus = 1

sõne = str(input("Sisesta sõne: "))

for täht in sõne:
    if täht in suludV:
        tasemesulud.append(suludV[suludV.index(täht)]) #lisab taseme sulu listi
        tase +=1
        
    elif täht in suludP:
        try:
            if  suludV.index(tasemesulud[-1]) == suludP.index(täht): #vaatab kas tasemesulud sulguvad
                tasemesulud.pop(-1) #kui sulguvad kustutab viimase taseme sulu ära
                tase -=1
            
            else: # kui taseme sulg ei klappi seda sulguva suluga
                print("Sulud ei ole tasakaalus")
                tasakaalus = 0
                break
        except:
            print("Sulud ei ole tasakaalus")
            tasakaalus = 0
            break
        
if tase == 0 and tasakaalus == 1:
    print("Sulud on tasakaalus")
