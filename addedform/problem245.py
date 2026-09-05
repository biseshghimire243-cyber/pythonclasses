rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

for i in range(rows):
    print("Sum of row", i + 1, ":", sum(matrix[i]))