numbers = list(map(int, input("Enter numbers: ").split()))

max_digits = max(len(str(abs(n))) for n in numbers)

result = min(
    n for n in numbers
    if len(str(abs(n))) == max_digits
)

print("Result:", result)