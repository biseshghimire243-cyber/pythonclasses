class Member:

    def __init__(self, member_id, name, plan):
        self.member_id = member_id
        self.name = name
        self.plan = plan
        self.visits = 0

    def visit_gym(self):
        self.visits += 1
        print("Gym visit recorded.")

    def show_member(self):

        print("\n========== MEMBER ==========")
        print("ID:", self.member_id)
        print("Name:", self.name)
        print("Plan:", self.plan)
        print("Total Visits:", self.visits)


members = {}

while True:

    try:

        print("\n1. Add Member")
        print("2. Record Visit")
        print("3. View Member")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            member_id = input("Member ID: ")

            if member_id in members:
                raise ValueError("Member already exists.")

            name = input("Name: ")
            plan = input("Membership Plan: ")

            members[member_id] = Member(
                member_id,
                name,
                plan
            )

            print("Member added.")

        elif choice == 2:

            member_id = input("Member ID: ")

            if member_id not in members:
                raise ValueError("Member not found.")

            members[member_id].visit_gym()

        elif choice == 3:

            member_id = input("Member ID: ")

            if member_id not in members:
                raise ValueError("Member not found.")

            members[member_id].show_member()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)