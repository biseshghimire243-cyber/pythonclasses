rows = int(input("Enter number of rows: "))

matrix = []

for i in range(rows):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

for i, row in enumerate(matrix):
    row_range = max(row) - min(row)
    print(f"Range of row {i + 1}:", row_range)