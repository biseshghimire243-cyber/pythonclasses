marks = float(input("Enter marks: "))

if marks >= 90:
    grade_point = 4.0
elif marks >= 80:
    grade_point = 3.6
elif marks >= 70:
    grade_point = 3.2
elif marks >= 60:
    grade_point = 2.8
elif marks >= 50:
    grade_point = 2.4
elif marks >= 40:
    grade_point = 2.0
else:
    grade_point = 0.0

print("Grade Point:", grade_point)