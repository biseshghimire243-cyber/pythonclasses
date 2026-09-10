temperatures = list(map(float, input("Enter temperatures: ").split()))

total = sum(temperatures)
average = total / len(temperatures)

print("Total temperature:", total)
print("Average temperature:", round(average, 2))