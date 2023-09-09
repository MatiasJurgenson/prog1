võistlejadfail = open(str(input("Sisestage esimene fail: ")), encoding="utf-8" )
registreerimine = []

for rida in võistlejadfail:
    registreerimine.append(rida.strip().split(". "))    

võistlejadfail.close()

kohtfail = open(str(input("Sisestage teine fail: ")), encoding="utf-8" )
kolmasfail = open("tulemusfail", "w", encoding="utf-8" )

i = 1
for rida in kohtfail:
    kolmasfail.write(f"{i}. {registreerimine[int(rida) - 1][1]}\n")
    i += 1

kohtfail.close()
kolmasfail.close()