n = int(input("sisesta n: "))

i = 1
summa = 2
while i <= n:
    summa *= (2*i / (2*i - 1))*(2*i / (2*i + 1))
    i += 1
print("Korrutis on " + str(summa))