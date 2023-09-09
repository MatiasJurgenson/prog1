import math

def moos(suur, väike, kogus):
    vaja_suurt = math.floor(kogus / 5)
    if vaja_suurt <= suur:
        if kogus <= vaja_suurt * 5 + väike:
            vaja_väikseid = kogus - vaja_suurt * 5
            return vaja_väikseid + vaja_suurt
    else:
        if kogus <= suur * 5 + väike:
            vaja_väikseid = kogus - suur * 5
            return vaja_väikseid + suur
        
    return -1
print(moos(2, 20, 25))