temp = int(input("Mis temperatuur väljas on? "))
päike = str(input("Kas päike pastab? "))
lipp = str(input("Kas rannas lehvib roheline lipp?"))

if temp >= 0 and päike == "jah" or lipp == "jah":
    print("Võid minna randa!")
else:
    print("Täna ei tasu randa minna.")