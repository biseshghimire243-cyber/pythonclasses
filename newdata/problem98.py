students = {
    "Bishesh": 88,
    "Ram": 76,
    "Sita": 95,
    "Hari": 82,
    "Gita": 91
}

ranking = sorted(
    students.items(),
    key=lambda item: item[1],
    reverse=True
)

print("===== STUDENT RANKING =====")

rank = 1

for name, marks in ranking:
    print(rank, ".", name, "-", marks)
    rank += 1