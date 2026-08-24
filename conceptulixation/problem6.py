matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(2):
    row = []

    for j in range(2):
        row.append(matrix1[i][j] + matrix2[i][j])

    result.append(row)

print("Result:")

for row in result:
    print(row)