filename = "notes.txt"

try:

    with open(filename, "w") as file:

        file.write("Python File Handling\n")
        file.write("Learning Python is interesting.\n")
        file.write("Chapter 15 practice.\n")

    print("File created successfully.")

    with open(filename, "r") as file:

        content = file.read()

    print("\n========== FILE CONTENT ==========")
    print(content)

except FileNotFoundError:

    print("File not found.")

except PermissionError:

    print("Permission denied.")

except Exception as error:

    print("Error:", error)