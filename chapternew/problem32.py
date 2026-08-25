numbers = [11, 22, 33, 44, 55, 66, 77, 88]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even:", even)
print("Odd:", odd)