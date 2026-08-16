class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):

    def __init__(self, name, age, roll, course):
        super().__init__(name, age)

        self.roll = roll
        self.course = course

    def display(self):

        print(
            "Student:",
            self.name,
            "| Age:",
            self.age,
            "| Roll:",
            self.roll,
            "| Course:",
            self.course
        )


class Teacher(Person):

    def __init__(self, name, age, subject):
        super().__init__(name, age)

        self.subject = subject

    def display(self):

        print(
            "Teacher:",
            self.name,
            "| Age:",
            self.age,
            "| Subject:",
            self.subject
        )


class College:

    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):

        self.people.append(person)

        print("Person added successfully.")

    def display_people(self):

        print("\n==========", self.name, "==========")

        if not self.people:
            print("No records found.")
            return

        for person in self.people:

            person.display()


college = College("ABC College")

college.add_person(
    Student(
        "Bishesh",
        23,
        101,
        "BSc CSIT"
    )
)

college.add_person(
    Student(
        "Hari",
        22,
        102,
        "BSc CSIT"
    )
)

college.add_person(
    Teacher(
        "Ram Sir",
        35,
        "Python"
    )
)

college.add_person(
    Teacher(
        "Sita Ma'am",
        32,
        "Database"
    )
)

college.display_people()