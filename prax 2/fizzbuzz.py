arv = int(input("Sisestage täisarv: "))

s = ""

if arv % 3 == 0:
    s += "Fizz"
    
if arv % 5 == 0:
    s += "Buzz"
if s != "":
    print(s)
else:
    print(arv)
    
