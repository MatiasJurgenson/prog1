import pykkar

def vasakule():
    right()
    right()
    right()

def ümberpöörd():
    right()
    right()

#n = int(input("vaba ala suurus: "))
n = 5
maailm = ""

for i in range(n+2):
    if i == 0:
        maailm += "#"*(n+2) + "\n"
    elif i == n+1:
        maailm += "#"*(n+2) + "\n"
        
    
        
print(maailm)
        
        