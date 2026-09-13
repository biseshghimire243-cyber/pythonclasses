numbers = list(map(int, input("Enter numbers: ").split()))

even_numbers = [n for n in numbers if n % 2 == 0]

if even_numbers:
    print("Smallest even number:", min(even_numbers))
else:
    print("No even number found")