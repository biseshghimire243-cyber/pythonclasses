matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

result = []

for column in range(len(matrix[0])):
    new_row = []

    for row in range(len(matrix)):
        new_row.append(matrix[row][column])

    result.append(new_row)

print("Transpose:")

for row in result:
    print(row)