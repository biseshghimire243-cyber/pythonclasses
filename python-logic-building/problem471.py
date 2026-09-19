numbers = input("Enter numbers: ").split()

longest = ""

for number in numbers:
    if number == number[::-1] and len(number) > len(longest):
        longest = number

if longest:
    print("Longest palindrome number:", longest)
else:
    print("No palindrome number found")