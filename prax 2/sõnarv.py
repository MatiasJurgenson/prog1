# idee koodiks https://medium.com/@moulayjam/translate-your-digits-to-english-0-999-a8bd8030db85
print("Keel: inglise")
print("")

numbers0_20 = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thriteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
              "nineteen", "twenty"]

numbers30_100 = ["filler0", "filler1", "filler2", 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                 'eighty', 'ninety',] #võtsin need sealt samalt lehelt

number = int(input("Sisesta arv: "))

a = []
for num in str(number):
    a.append(int(num))

if number <= 20:
    print(str(numbers0_20[number]))

elif number < 100:
    a = []
    for num in str(number):
        a.append(int(num))
    print(str(numbers30_100[a[0]]) + " " +str(numbers0_20[a[1]]))

else:
    print(str(numbers0_20[a[0]]) + " hundred "+ str(numbers30_100[a[1]]) + " " + str(numbers0_20[a[2]]))
    