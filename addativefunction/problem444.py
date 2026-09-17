rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

total = 0

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            total += matrix[i][j]

print("Border sum:", total)