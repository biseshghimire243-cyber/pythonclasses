class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.marks = []

    def add_marks(self):

        self.marks.clear()

        for i in range(5):

            mark = float(
                input(f"Subject {i + 1} marks: ")
            )

            if mark < 0 or mark > 100:
                raise ValueError(
                    "Marks must be between 0 and 100."
                )

            self.marks.append(mark)

    def calculate_result(self):

        total = sum(self.marks)
        percentage = total / len(self.marks)

        if percentage >= 80:
            grade = "A"

        elif percentage >= 70:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 50:
            grade = "D"

        else:
            grade = "F"

        return total, percentage, grade

    def show_result(self):

        total, percentage, grade = (
            self.calculate_result()
        )

        print("\n========== RESULT ==========")
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Marks:", self.marks)
        print("Total:", total)
        print("Percentage:", percentage)
        print("Grade:", grade)


students = {}

while True:

    try:

        print("\n1. Add Student")
        print("2. Enter Marks")
        print("3. View Result")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            roll = input("Roll: ")

            if roll in students:
                raise ValueError("Student exists.")

            name = input("Name: ")

            students[roll] = Student(
                name,
                roll
            )

            print("Student added.")

        elif choice == 2:

            roll = input("Roll: ")

            if roll not in students:
                raise ValueError("Student not found.")

            students[roll].add_marks()

        elif choice == 3:

            roll = input("Roll: ")

            if roll not in students:
                raise ValueError("Student not found.")

            students[roll].show_result()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)