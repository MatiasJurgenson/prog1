def kankaan(n):
    if n == 1:
        return 2
    else:
        return kankaan(n - 1) * 2 - 1
    
#print(kankaan(10))