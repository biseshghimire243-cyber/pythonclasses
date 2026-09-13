start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

total = 0

for number in range(start, end + 1):
    total += number

print("Sum:", total)