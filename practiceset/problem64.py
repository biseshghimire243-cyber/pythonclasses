try:
    student_id = input("Enter Student ID: ")

    if len(student_id) != 6:
        raise Exception("Student ID must contain exactly 6 characters.")

    print("Student ID:", student_id)

except Exception as e:
    print(e)