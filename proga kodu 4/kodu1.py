i = int(input("Sisesta arv: "))
sammude_arv = 0
while i > 1:
    if i % 2 == 0:
        i /= 2
        sammude_arv += 1
    else:
        i = (i*3 + 1)
        sammude_arv += 1
print("Sammude arv on " + str(sammude_arv) + ".")