number = int(input("Enter number: "))
multiple = int(input("Enter multiple: "))

lower = (number // multiple) * multiple
upper = lower + multiple

if abs(number - lower) <= abs(number - upper):
    nearest = lower
else:
    nearest = upper

print("Nearest multiple:", nearest)