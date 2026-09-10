distances = list(map(float, input("Enter distances for each stop: ").split()))

total = 0

for distance in distances:
    total += distance

print("Total journey distance:", total)