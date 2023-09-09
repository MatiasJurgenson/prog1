def teisenda(r, g, b): #0.1, 0.3, 0.9
    listrgb = [r, g, b]
    
    xmin = min(listrgb)
    xmax = max(listrgb)
    
    l = (xmin + xmax) / 2 # heledus
    
    if xmin == xmax: #Kui Xmin ja Xmax on võrdsed, siis toon on H = 0 ja küllastus S = 0
      h = 0
      s = 0
    else:
        if xmax == r:
            h = (g - b) / (xmax - xmin)

        if xmax == g:
            h = 2 + (b - r) / (xmax - xmin)

        if xmax == b:
            h = 4 + (r - g) / (xmax - xmin)
            
    #Kui H < 0, siis H = H + 6. Need valemid annavad H väärtuse vahemikus 0 kuni 6. Seetõttu korrutame tulemuse veel 60-ga, et saada väärtus kraadides
    if h < 0:
        h += 6
    h *= 60
    
    if l < 1/2:
        s = (xmax - xmin) / (xmax + xmin)

    else:
        s = (xmax - xmin) / (2 - xmax - xmin)
    
    return h, s, l

#print(teisenda(0.1, 0.3, 0.9))
#print(teisenda(0.4, 0.4, 0.4))