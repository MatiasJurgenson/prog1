import json
from urllib.request import urlopen
import matplotlib.pyplot as plt

url = "https://opendata.digilugu.ee/opendata_covid19_test_county_all.json"
response = urlopen(url)

data = json.loads(response.read())

print(data[0])
print(data[1])
print(data[3])

päevade_arv = len(data) / 34

#küsib kasutajalt maakonna nime
maakond = str(input("Sisestage maakond: "))

#koostab järgmised graafikud, mis kujutavad muutumist ajas:
#positiivsete testide koguarv antud maakonnas igal päeval;
päevatestide_arv = []
päevad = []
protsent = []
for i in data:
    if i['County'] == maakond and i['ResultValue'] == 'P':
        postestide_arv = i['DailyTests']
        päevatestide_arv.append(postestide_arv)
        try:
            protsent.append(postestide_arv / (postestide_arv + negtestide_arv) * 100)
        except:
            protsent.append(0)
        
        päev = i['StatisticsDate']
        päevad.append(päev)
    elif i['County'] == maakond and i['ResultValue'] == 'N':
        negtestide_arv = i['DailyTests']
        
    
plt.plot(päevad, päevatestide_arv)
plt.ylabel('positiivsete testide koguarv')
plt.xlabel('päevade arv')
plt.show()
          
#positiivsete testide protsent kõigi tehtud testide hulgas antud maakonnas igal päeval.

plt.plot(päevad, protsent)
plt.ylabel('positiivsete testide protsent')
plt.xlabel('päevade arv')
plt.show()



