rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(float, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

for i, row in enumerate(matrix):
    average = sum(row) / len(row)
    print(f"Row {i + 1} average:", round(average, 2))