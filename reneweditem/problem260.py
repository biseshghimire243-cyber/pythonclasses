n = int(input("Enter matrix size: "))

matrix = []

for _ in range(n):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("Matrix is symmetric.")
else:
    print("Matrix is not symmetric.")