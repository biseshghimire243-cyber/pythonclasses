class Father:

    def father_property(self):
        print("Father owns a house.")


class Mother:

    def mother_property(self):
        print("Mother owns jewelry.")


class Child(Father, Mother):

    def child_details(self):
        print("Child inherits properties from both parents.")


child = Child()

child.father_property()
child.mother_property()
child.child_details()