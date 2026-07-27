student = {
    "name": "Bishesh",
    "age": 23
}

try:
    key = input("Enter key: ")
    print(student[key])

except KeyError:
    print("Key not found.")