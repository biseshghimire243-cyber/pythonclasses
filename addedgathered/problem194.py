numbers = list(map(int, input("Enter numbers: ").split()))

even_numbers = [num for num in numbers if num % 2 == 0]

if even_numbers:
    average = sum(even_numbers) / len(even_numbers)
    print("Average of even numbers:", average)
else:
    print("No even numbers found.")