class Student:

    def __init__(self, name, roll, course, marks):
        self.name = name
        self.roll = roll
        self.course = course
        self.marks = marks

    def calculate_percentage(self):

        total = sum(self.marks)

        percentage = total / len(self.marks)

        return percentage

    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        else:
            return "F"

    def display_student(self):

        print("\n========== STUDENT DETAILS ==========")

        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("Course:", self.course)

        print("Marks:", self.marks)

        percentage = self.calculate_percentage()
        grade = self.calculate_grade()

        print("Percentage:", percentage)
        print("Grade:", grade)


# Taking input from user

name = input("Enter student name: ")
roll = input("Enter roll number: ")
course = input("Enter course: ")

marks = []

print("\nEnter marks for 5 subjects:")

for i in range(5):

    mark = float(
        input(f"Subject {i + 1}: ")
    )

    if mark < 0 or mark > 100:
        print("Invalid marks.")
        exit()

    marks.append(mark)


student = Student(
    name,
    roll,
    course,
    marks
)


student.display_student()