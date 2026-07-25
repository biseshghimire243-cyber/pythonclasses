student = {
    "name": "Bishesh",
    "age": 23
}

try:
    print(student["address"])

except KeyError:
    print("Key not found.")