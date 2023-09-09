andmed = [6, 7, 0, 0, 6, 7, 0, 0, 2, 3]
andmed = [16, 51, 27, 42, 22, 0, 0, 0,
          3, 44, 0, 39, 42, 10, 25,
          38, 0, 33, 29, 0, 0, 3, 0,
          19, 24, 0, 39, 0, 33, 13, 6,
          0, 6, 0, 0, 0, 38, 31, 31,
          0, 10, 10, 0, 6, 51, 0, 0,
          0, 0, 0, 33, 0, 33, 10, 0]

nakatajad = []

for i in range(len(andmed)):
    if andmed[i] != 0 and andmed[i] not in nakatajad:
        nakatajad.append(andmed[i])
s = ""
for nakataja in nakatajad:
    s += f" {nakataja}"        
print(f"Nakatajad on:{s}")

lähtepunktid = []
edasikandjad = []
for i in nakatajad:
    if andmed[i-1] != 0:
        edasikandjad.append(i)
    elif andmed[i-1] == 0:
        lähtepunktid.append(i)
        
s = ""
for edasikandja in edasikandjad:
    s += f" {edasikandja}"
print(f"Nakkuse edasikandjad on:{s}")

s = ""
for lähtepunkt in lähtepunktid:
    s += f" {lähtepunkt}"
print(f"Nakkuse lähtepunktid on:{s}")
        