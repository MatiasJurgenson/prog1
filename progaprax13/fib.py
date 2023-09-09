sõnastik = {1:1, 2:1}

def fib(n):
    if n == 1 or n == 2: return 1
    
    n1 = n -1
    
    if n1 not in sõnastik:
        arv = fib(n-1)
        sõnastik[n1] = arv
        
    else:
        arv = sõnastik[n1]
        
    
    
    return arv + sõnastik[n-2]
    
    
    
    
print(fib(986))
print("")

def fib2(n):
    if n <= 2: return 1
    
    return fib2(n-1) + fib2(n-2)

import functools

@functools.cache
def fib3(n):
    if n <= 2: return 1
    
    return fib3(n-1) + fib3(n-2)

print(fib3(493))

