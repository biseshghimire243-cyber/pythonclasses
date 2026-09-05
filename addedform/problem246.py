rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

for j in range(cols):
    total = 0

    for i in range(rows):
        total += matrix[i][j]

    print("Sum of column", j + 1, ":", total)