from datetime import date #sain reactgo.com -ist

#date.today().year

def päevade_arv(x):
    kuud = [29, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if x > 12 or x < 1:
        return -1
    elif date.today().year % 4 == 0 and x == 2:
        return kuud[0]
    else:
        return kuud[x]

while True:
    try:
        kuu = (input("Sisesta kuu number: "))
        if kuu == "":
            break
        kuu = int(kuu)
    except ValueError:
        print("Ebakorrektne number")
        continue
    if kuu not in [1,2,3,4,5,6,7,8,9,10,11,12]:
        print("Kuu number peab jääma lõiku 1–12")
        continue
    else:
        print(" Selles kuus on " + str(päevade_arv(kuu)) + " päeva")
    
print("Programm lõpetas töö.")       
    