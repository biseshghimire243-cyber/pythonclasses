number = input("Enter a number: ")

even_sum = 0
odd_sum = 0

for digit in number:
    value = int(digit)

    if value % 2 == 0:
        even_sum += value
    else:
        odd_sum += value

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)