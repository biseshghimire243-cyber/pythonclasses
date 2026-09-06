rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

for _ in range(rows):
    row = list(map(int, input("Enter row (0/1): ").split()))
    grid.append(row)

visited = set()


def explore(r, c):
    if (
        r < 0 or r >= rows or
        c < 0 or c >= cols or
        grid[r][c] == 0 or
        (r, c) in visited
    ):
        return

    visited.add((r, c))

    explore(r + 1, c)
    explore(r - 1, c)
    explore(r, c + 1)
    explore(r, c - 1)


islands = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1 and (i, j) not in visited:
            islands += 1
            explore(i, j)

print("Number of islands:", islands)