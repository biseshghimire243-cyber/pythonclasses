start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

result = []

for number in range(start, end + 1):
    if number % 3 == 0 and number % 5 == 0:
        result.append(number)

print("Numbers divisible by both 3 and 5:", result)