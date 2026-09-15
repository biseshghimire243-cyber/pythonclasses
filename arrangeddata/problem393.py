numbers = list(map(int, input("Enter numbers: ").split()))

odd_numbers = [n for n in numbers if n % 2 != 0]

if odd_numbers:
    difference = max(odd_numbers) - min(odd_numbers)
    print("Difference:", difference)
else:
    print("No odd numbers found")