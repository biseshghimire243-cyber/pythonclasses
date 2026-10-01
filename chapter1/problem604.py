numbers = list(map(int, input("Enter numbers: ").split()))

result = max(numbers, key=lambda n: len(str(abs(n))))

print("Number with most digits:", result)
print("Number of digits:", len(str(abs(result))))