kortermaja = {1: {1: 'Juhan',2: 'Maili', 3: 'Karin'}, 2: {4: 'Teet', 5: 'Robert'}, 3: {6: 'Meelis'}}

def väljasta_kortermaja(a):
    korrus = 1
    for korrus in a:
        korruselist = str(korrus) + " - "
        for korter in a[korrus]:
            korruselist += str(korter) + ": " + str(a[korrus][korter]) + "; "
        print(korruselist)
        korrus += 1

def leia_omanik(a, b):
    korrus = 1
    for korrus in a:
        for korter in a[korrus]:
            if a[korrus][korter] == b:
                return (korrus, korter)
        korrus += 1
    return (0, 0)

def muuda_omanikku(a,b,c):
    korrus = 1
    for korrus in a:
        for korter in a[korrus]:
            if korter == b:
                a[korrus][b] = c
                return True
        korrus += 1
    return False

print("kortemaja korterite omanikud: ")
väljasta_kortermaja(kortermaja)

vana = str(input("Vana omaniku nimi: "))
korter = leia_omanik(kortermaja, vana) 
if korter == (0,0):
    print(vana + " pole ühegi korteri omanik.")
else:
    print(vana + " elab " + str(korter[0]) + ". korrusel korteris nr " + str(korter[1]) + ".")

uus = str(input("Uue omaniku nimi: "))
muuda_omanikku(kortermaja, korter[1], uus)
print("Kortermaja korterite omanikud pärast omanike vahetust: ")
väljasta_kortermaja(kortermaja)
    
