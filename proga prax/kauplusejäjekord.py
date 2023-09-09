esemed = str(input("Sisesta esemete arvud: "))#2 4 10 8 3 1 12 5 2 1 7
esemederaldi = esemed.split(" ")

print(f"Järjekorras seisab {len(esemederaldi)} inimest")

korvis = 0
for i in range(len(esemederaldi)):
    esemederaldi[i] = int(esemederaldi[i]) #jär = [int(x) for x in jär]
    if esemederaldi[i] > 3:
        korvis += 1

print(f"Rohkem kui kolm eset on korvis {korvis} inimesel")

print(f"Kõige rohkem esemeid on {esemederaldi.index(max(esemederaldi)) + 1}. inimesel, kellel on {max(esemederaldi)} eset")
        