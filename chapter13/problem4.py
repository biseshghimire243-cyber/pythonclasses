try:
    file = open("student.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File does not exist.")