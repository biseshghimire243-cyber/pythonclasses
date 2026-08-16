class Teacher:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display(self):
        print("Teacher:", self.name)
        print("Subject:", self.subject)


class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Student:", self.name)
        print("Roll:", self.roll)


class School:

    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_student(self, student):
        self.students.append(student)

    def display(self):

        print("\n========== SCHOOL ==========")
        print("School:", self.name)

        print("\nTeachers:")

        for teacher in self.teachers:
            teacher.display()

        print("\nStudents:")

        for student in self.students:
            student.display()


school = School("ABC College")

school.add_teacher(
    Teacher("Ram", "Python")
)

school.add_teacher(
    Teacher("Sita", "Database")
)

school.add_student(
    Student("Bishesh", 101)
)

school.add_student(
    Student("Hari", 102)
)

school.display()