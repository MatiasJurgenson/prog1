def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return auto_hind(round(0.8*hind, 2), aastad-1)
    
#print(auto_hind(8000.0, 5))