numbers = list(map(int, input("Enter numbers: ").split()))

odd_numbers = [n for n in numbers if n % 2 != 0]

if odd_numbers:
    average = sum(odd_numbers) / len(odd_numbers)
    print("Average of odd numbers:", average)
else:
    print("No odd numbers found")