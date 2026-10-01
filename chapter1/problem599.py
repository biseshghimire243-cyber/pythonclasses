numbers = list(map(int, input("Enter numbers: ").split()))

odd_numbers = [n for n in numbers if n % 2 != 0]

if odd_numbers:
    print("Smallest odd number:", min(odd_numbers))
else:
    print("No odd number found")