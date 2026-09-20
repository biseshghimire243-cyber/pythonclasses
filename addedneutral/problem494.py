numbers = list(map(int, input("Enter numbers: ").split()))

start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

expected = set(range(start, end + 1))
actual = set(numbers)

missing = sorted(expected - actual)

if missing:
    print("Missing numbers:", missing)
else:
    print("No numbers are missing.")