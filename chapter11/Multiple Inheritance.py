class Father:

    def money(self):
        print("Father's Money")

class Mother:

    def love(self):
        print("Mother's Love")

class Child(Father, Mother):
    pass

c = Child()

c.money()
c.love()