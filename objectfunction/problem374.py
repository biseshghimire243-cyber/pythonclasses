numbers = list(map(int, input("Enter numbers: ").split()))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

count = 0

for number in numbers:
    if low <= number <= high:
        count += 1

print("Numbers in range:", count)