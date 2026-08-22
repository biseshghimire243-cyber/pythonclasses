name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))

average = (math + science + computer) / 3

print("\nStudent:", name)
print("Average:", average)

if average >= 80:
    print("Performance: Excellent")
elif average >= 60:
    print("Performance: Good")
elif average >= 40:
    print("Performance: Average")
else:
    print("Performance: Poor")