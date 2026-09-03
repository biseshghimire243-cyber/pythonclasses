start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

numbers = []

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        numbers.append(num)

print("Numbers divisible by both 3 and 5:", numbers)