size = int(input("Enter matrix size: "))

matrix = []

for i in range(size):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

product = 1

for i in range(size):
    product *= matrix[i][i]

print("Diagonal product:", product)