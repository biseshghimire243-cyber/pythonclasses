members = {}

while True:

    try:

        print("\n========== GYM MEMBERSHIP SYSTEM ==========")
        print("1. Add Member")
        print("2. View Members")
        print("3. Search Member")
        print("4. Remove Member")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            member_id = input("Member ID: ")

            if member_id in members:
                raise Exception("Member already exists.")

            name = input("Member Name: ")
            age = int(input("Age: "))
            plan = input("Membership Plan (Monthly/Yearly): ")

            members[member_id] = {
                "Name": name,
                "Age": age,
                "Plan": plan
            }

            print("Member Added Successfully.")

        elif choice == 2:

            if len(members) == 0:
                print("No Members Found.")

            else:

                print("\n===== MEMBER LIST =====")

                for member_id, info in members.items():

                    print("------------------------")
                    print("ID :", member_id)
                    print("Name :", info["Name"])
                    print("Age :", info["Age"])
                    print("Plan :", info["Plan"])

        elif choice == 3:

            member_id = input("Member ID: ")

            if member_id not in members:
                raise Exception("Member Not Found.")

            print(members[member_id])

        elif choice == 4:

            member_id = input("Member ID: ")

            if member_id not in members:
                raise Exception("Member Not Found.")

            del members[member_id]

            print("Member Removed Successfully.")

        elif choice == 5:

            print("Thank You!")
            break

        else:

            print("Invalid Choice.")

    except Exception as e:
        print(e)