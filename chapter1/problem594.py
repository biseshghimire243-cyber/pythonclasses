numbers = list(map(int, input("Enter numbers: ").split()))

def digit_sum(number):
    return sum(int(d) for d in str(abs(number)))

result = min(numbers, key=digit_sum)

print("Number:", result)
print("Digit sum:", digit_sum(result))