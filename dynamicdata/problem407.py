number = int(input("Enter a number: "))

lower = (number // 10) * 10
upper = lower + 10

if number - lower < upper - number:
    nearest = lower
else:
    nearest = upper

print("Nearest multiple of 10:", nearest)