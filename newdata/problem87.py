matrix = [
    [5, 2, 3],
    [4, 8, 6],
    [7, 1, 9]
]

main_diagonal = 0
secondary_diagonal = 0

for i in range(len(matrix)):
    main_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][len(matrix) - 1 - i]

print("Main diagonal sum:", main_diagonal)
print("Secondary diagonal sum:", secondary_diagonal)