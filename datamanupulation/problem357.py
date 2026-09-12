numbers = input("Enter numbers separated by spaces: ").split()

longest = numbers[0]

for number in numbers:
    if len(number) > len(longest):
        longest = number

print("Number with most digits:", longest)
print("Number of digits:", len(longest))