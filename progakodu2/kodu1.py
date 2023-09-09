from random import sample
#sample(range(1, 5), 2)

def bingo():
    väiksed = [1,2,3]
    while 1 in väiksed and 2 in väiksed and 3 in väiksed:
        väiksed = sample(range(1, 11), 3)
    väiksed.extend(sample(range(11, 21), 2))
    return väiksed
    
    
    
print(bingo())