numbers = [12, 15, 22, 31, 44, 57, 68, 73]

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)