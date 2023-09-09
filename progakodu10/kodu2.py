def võitja(maatriks):
    Xvõite = 0
    Ovõite = 0
    
    for i in range(2):#vertikaal kontrollija
        for num, el in enumerate(maatriks[i]):
            if el == "O":
                if maatriks[i][num] == "O" and maatriks[i+1][num] == "O" and maatriks[i+2][num] == "O":
                   Ovõite += 1
            elif el == "X":
                if maatriks[i][num] == "X" and maatriks[i+1][num] == "X" and maatriks[i+2][num] == "X":
                   Xvõite += 1

    for rida in maatriks: # horisontaalne
        for i in range(2):
            if rida[i] == "O":
                if rida[i] == "O" and rida[i+1] == "O" and rida[i+2] == "O":
                    Ovõite += 1
            elif rida[i] == "X":
                if rida[i] == "X" and rida[i+1] == "X" and rida[i+2] == "X":
                    Xvõite += 1
                    
    for i in range(2):#diagonaali kontrollija
        for num, el in enumerate(maatriks[i]):
            if num < 2:
                if el == "O":
                    if maatriks[i][num] == "O" and maatriks[i+1][num+1] == "O" and maatriks[i+2][num+2] == "O":
                       Ovõite += 1
                elif el == "X":
                    if maatriks[i][num] == "X" and maatriks[i+1][num+1] == "X" and maatriks[i+2][num+2] == "X":
                       Xvõite += 1
            else:
                if el == "O":
                    if maatriks[i][num] == "O" and maatriks[i+1][num-1] == "O" and maatriks[i+2][num-2] == "O":
                       Ovõite += 1
                elif el == "X":
                    if maatriks[i][num] == "X" and maatriks[i+1][num-1] == "X" and maatriks[i+2][num-2] == "X":
                       Xvõite += 1
      
                    
    return {'O': Ovõite, 'X': Xvõite}

                    
print(võitja([[' ', ' ', ' ', 'O'],
              [' ', 'X', 'O', ' '],
              [' ', 'O', 'X', ' '],
              [' ', ' ', ' ', 'X']]))
        