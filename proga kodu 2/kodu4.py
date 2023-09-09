tulu = int(input("Sisesta aastatulu: "))

if tulu < 6000:
    a = tulu
elif tulu >= 6000 and tulu < 14400:
    a = 6000
elif tulu >= 14400 and tulu < 25200:
    a = 6000 - 6000 / 10800 * (tulu - 14400)
else:
    a = 0
print("Maksuvaba tulu on " + str(round(a, 2)) + " eurot.")