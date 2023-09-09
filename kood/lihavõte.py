aasta = int(input("sisesta aasta: "))
# 1 samm
a = aasta % 19
# 2 samm
b = aasta // 100
c = aasta % (b*100)
# 3 samm
d = b // 4
e = b % (d*4)
# 4 samm
f = (b + 8) // 25
# 5 samm
g = (b - f + 1) // 3
# 6 samm
h = (19 * a + b - d - g + 15) % 30
# 7 samm
i = c // 4
j = c % (i*4)
# 8 samm
k = (32 + 2 * e + 2 * i - h - j) % 7
# 9 samm
l = (a + 11 * h + 22 * k) // 451
# 10 samm
m = (h + k - 7 * l + 114) // 31
n = (h + k - 7 * l + 114) % (31*m)

print(str(n+1) + "-" + str(m) + "-" + str(aasta))