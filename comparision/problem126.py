student1 = float(input("Enter Student 1 marks: "))
student2 = float(input("Enter Student 2 marks: "))

if student1 > student2:
    print("Student 1 scored higher")
elif student2 > student1:
    print("Student 2 scored higher")
else:
    print("Both students scored equal marks")