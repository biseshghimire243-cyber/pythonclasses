rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

best_row = 0
best_sum = sum(matrix[0])

for i in range(1, rows):
    row_sum = sum(matrix[i])

    if row_sum > best_sum:
        best_sum = row_sum
        best_row = i

print("Row with highest sum:", best_row + 1)
print("Sum:", best_sum)