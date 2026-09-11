first = float(input("Enter first term: "))
ratio = float(input("Enter common ratio: "))
terms = int(input("Enter number of terms: "))

total = 0
current = first

for _ in range(terms):
    total += current
    current *= ratio

print("Sum:", total)