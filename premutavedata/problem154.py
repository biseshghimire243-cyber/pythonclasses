number = int(input("Enter a number: "))

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i

if total == number:
    print("Perfect number")
else:
    print("Not a perfect number")