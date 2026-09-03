marks = list(map(float, input("Enter marks of subjects: ").split()))

total = sum(marks)
percentage = total / len(marks)

print("Total marks:", total)
print("Percentage:", percentage, "%")