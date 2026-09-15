city1 = input("Enter first city: ")
temp1 = float(input("Enter temperature: "))

city2 = input("Enter second city: ")
temp2 = float(input("Enter temperature: "))

difference = abs(temp1 - temp2)

print(city1, "temperature:", temp1)
print(city2, "temperature:", temp2)
print("Temperature difference:", difference)