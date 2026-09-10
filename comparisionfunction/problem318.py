n = int(input("Enter matrix size: "))

matrix = []

for i in range(n):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    matrix.append(row)

main_sum = 0
secondary_sum = 0

for i in range(n):
    main_sum += matrix[i][i]
    secondary_sum += matrix[i][n - 1 - i]

print("Main diagonal sum:", main_sum)
print("Secondary diagonal sum:", secondary_sum)