temp1 = float(input("Enter today's temperature: "))
temp2 = float(input("Enter yesterday's temperature: "))

if temp1 > temp2:
    print("Today is hotter")
elif temp1 < temp2:
    print("Today is colder")
else:
    print("Temperature is the same")