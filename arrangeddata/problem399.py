marks = list(map(float, input("Enter subject marks: ").split()))
best_count = int(input("How many best subjects to include? "))

marks.sort(reverse=True)

selected = marks[:best_count]
total = sum(selected)

print("Selected marks:", selected)
print("Total:", total)
print("Average:", total / len(selected))