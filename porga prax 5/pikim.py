pikimsõna = []

fail = open("lemmad.txt", encoding="UTF-8") #oleks tahtnud 2013 aga see ei laadinud alla

for rida in fail:

    rida = rida.strip("\n")
    i = -1
    try:
        for täht in rida:
            if rida.count(täht) >= 2: # counti sain proga õpikust
                ValueError
        pikimsõna.append(rida) 
    except:
        continue
fail.close()            
print(f"{max(mylist, key=len)}") # stackoverflowst saadud leiab kõige suurema sõne
            
                
                
                
            
            