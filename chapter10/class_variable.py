class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Ram")
s2 = Student("Hari")

print(s1.school)
print(s2.school)