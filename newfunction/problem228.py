n = int(input("Enter matrix size: "))

matrix = []

for i in range(n):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

main_diagonal = 0
secondary_diagonal = 0

for i in range(n):
    main_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][n - 1 - i]

print("Main diagonal:", main_diagonal)
print("Secondary diagonal:", secondary_diagonal)
print("Absolute difference:", abs(main_diagonal - secondary_diagonal))